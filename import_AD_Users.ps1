Import-Module ActiveDirectory
$Domain="@abc.com"
$UserOu="OU=Users,DC=abc,DC=com" $NewUsersList=Import-CSV "D:\students.csv"
ForEach ($User in $NewUsersList)
{
$givenName=$User.givenName $sAMAccountName=$User.sAMAccountName $userPrincipalName=$User.sAMAccountName+$Domain $userPassword=$User.Password $expire=$null
New-ADUser -Name $givenName -GivenName $givenName -SamAccountName $sAMAccountName
}
