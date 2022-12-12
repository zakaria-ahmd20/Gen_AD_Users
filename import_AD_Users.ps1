Import-Module ActiveDirectory
$ADUsers = Import-Csv C:\users.csv
foreach ($User in $ADUsers) {
    $Name = $User.Name
    $username = $User.username
    $password = $User.passcode
    $Title=$User.Title
    New-ADUser -Name $Name -SamAccountName $username -AccountPassword (ConvertTo-secureString $password -AsPlainText -Force) -Title $Title
    Enable-AdAccount -Identity $username
    }
