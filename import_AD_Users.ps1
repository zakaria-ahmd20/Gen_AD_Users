Import-Module ActiveDirectory
$ADUsers = Import-Csv C:\users.csv
foreach ($User in $ADUsers) {
    $FirstName = $User.FirstName
    $LastName = $User.LastName
    $username =  $FirstName.$LastName
    $password = $User.passcode
    $Title = $User.Title
    $Manager_Email = $User.Manager_Email
    New-ADUser -Name $Name -SamAccountName $username -AccountPassword (ConvertTo-secureString $password -AsPlainText -Force) -Title $Title -ChangePasswordAtLogon $true
    Enable-AdAccount -Identity $username
    }
