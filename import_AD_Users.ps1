Import-Module ActiveDirectory # imports module
$ADUsers = Import-Csv C:\students.csv 
foreach ($User in $ADUsers) {
    $username = $User.username
    $password = $User.passcode
    New-ADUser -Name $username -AccountPassword (ConvertTo-secureString $password -AsPlainText -Force) -ChangePasswordAtLogon $True
    
    
    
    
    }
