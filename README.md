I encountered an encoding problem, after executing the command **solution.py -> solution.js -> solution2.py**
files with utf-16 encoding are generated (by default, win powershell does this).
Therefore, I use other commands:
**py solution.py | Set-Content -Path solution.js -Encoding utf8NoBOM**
**node solution.js | Set-Content -Path solution2.py -Encoding utf8NoBOM**
**Compare-Object (Get-Content solution.py) (Get-Content solution2.py)**
