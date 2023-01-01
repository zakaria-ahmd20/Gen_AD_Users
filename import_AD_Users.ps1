Import-Module ActiveDirectory
$ADUsers = Import-Csv C:\users.csv # or path of pyhton code
foreach ($User in $ADUsers) {
    $FirstName = $User.FirstName
    $LastName = $User.LastName
    $username =  $FirstName.$LastName
    $password = $User.passcode
    $Title = $User.Title
    $Manager_Email = $User.Manager_Email
    New-ADUser -Name $Name -SamAccountName $username -AccountPassword (ConvertTo-secureString $password -AsPlainText -Force) -Title $Title 
    Enable-AdAccount -Identity $username
    Set-ADUser -Identity $username -ChangePasswordAtLogon $true
    }
