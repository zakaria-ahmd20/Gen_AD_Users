Import-Module ActiveDirectory
$Log_File = C:\PS\Logs\$env:UserName_ad_script.log
if (Test-Path $Log_File) {
    echo "logging to $Log_File"
}
else {
    New-Item $Log_File -ItemType Directory
    echo "Log file created ....."
}
Start-Transcript -path $Log_File -append
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
Stop-Transcript
