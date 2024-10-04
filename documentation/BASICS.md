## Console Basics
```
   ____________
  < terasploit >
   ------------
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
```
Terasploit has a basic usage, no need to worry as terasploit framework is not very hard to use, specially if you have
already used metasploit framework. Terasploit is heavily based on metasploit framework. Terasploit is an exploitation
framework too, but not as great as metasploit ofcourse.

## Console Commands
```
tsf > help

Core Commands
=============

   Name              Description
   ────              ───────────
   banner            Display banner
   set               Inserts a value on the specified parameter
   show              Display specified parameter contents
   unset             Removes a value on the specified parameter
   options           Display current module options available (shortcut command)
   search            Finds a module by matching str characters from module path list


Module Commands
===============

   Name              Description
   ────              ───────────
   back              Unuse the current module
   exploit           Execute command for exploit module
   info              Display full module information
   run               Execute command for non-exploit module
   use               Interact with a module


tsf >
```

### Banner
The command "Banner" does not do anything important, it's just there to reprint the banner if the user wants to see cool
banners of terasploit framework.

### Set/Unset
The command "Set" is used when inserting a value from a specified parameter in current available options. The unset on 
the other hand will remove a value from the specified parameter.

### Show/Options
The command "Show" is used to display contents of the specified parameter. One of its shortcut command is "options" which
displays all available module options.

### Search
The command "Search" is used for searching modules. It searches for module by matching str words from freshly gathered 
module paths, if the str word matched one or more module, it will display its path and description.

### Back/Use
The command "Back" is used to unuse module, Use command on the other hand will import the module to allow user to
interact with the module and perform its task.

### Info
The command "Info" is used for dumping the module's information. For module developers, the module information is an
important part as the framework function will base on what's in the module information. For example: in module info,
if the module value is auxiliary, it will treat the module as a non-exploit module.

### Exploit/Run
As stated in the "Info" command, these two command has an obvious difference. Exploit is for executing exploit modules
and run is for non-exploit module. The thing here is that exploit is not a console function, but a module class
function. It means that if one of the two commands were used, the console will check whether the command you used is
an existing attribute from module class, if its not then it will raise an unknown command error.

### Basic usage
```
tsf > use exploit/multi/handler
[*] Using module default payload, payload/generic/shell_reverse_tcp
tsf exploit(multi/handler) > show options

Payload options (payload/generic/shell_reverse_tcp):

   Name    Current Settings  Required  Description
   ────    ────────────────  ────────  ───────────
   LHOST                     yes       target listening address
   LPORT   4444              yes       target listening port



To view the full module information, use 'info <path>' command.

tsf exploit(multi/handler) > set lhost 0.0.0.0
lhost => 0.0.0.0
tsf exploit(multi/handler) > exploit
```
