# Prompt for AD credentials securely
$credential = Get-Credential -Message "Enter AD credentials"

# Specify the log file path
$Log_File = "C:\PS\Logs\$env:UserName_ad_script.log"

# Start transcript for logging
Start-Transcript -Path $Log_File -Append

# Check if the log file exists
if (Test-Path $Log_File) {
    Write-Host "Logging to $Log_File"
} else {
    New-Item $Log_File -ItemType File | Out-Null
    Write-Host "Log file created ..."
}

# Import user details from CSV
$ADUsers = Import-Csv C:\users.csv

foreach ($User in $ADUsers) {
    $FirstName = $User.FirstName
    $LastName = $User.LastName
    $username = $FirstName + $LastName
    $password = $User.passcode
    $Title = $User.Title
    $Manager_Email = $User.Manager_Email

    try {
        # Check if the user already exists
        $AdUser_exists = Get-ADUser -Filter {SamAccountName -eq $username} -ErrorAction Stop

        if ($AdUser_exists) {
            Write-Host "User $username already exists."
            continue
        }
    } catch {
        # Log error when checking user existence
        $errorMessage = "Error checking user existence for $username: $_"
        Write-Host $errorMessage
        Add-Content -Path $Log_File -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - $errorMessage"
        continue
    }

    try {
        # Set user details
        $Name = "$FirstName $LastName"
        $userParams = @{
            SamAccountName  = $username
            UserPrincipalName = "$username@yourdomain.com" # Update with your actual domain
            Name            = $Name
            GivenName       = $FirstName
            Surname         = $LastName
            Title           = $Title
            AccountPassword = (ConvertTo-SecureString $password -AsPlainText -Force)
            Enabled         = $true
        }

        # Create new AD user
        New-ADUser @userParams -Credential $credential -ErrorAction Stop

        # Set manager if Manager_Email is provided
        if ($Manager_Email) {
            $Manager = Get-ADUser -Filter {UserPrincipalName -eq $Manager_Email} -ErrorAction Stop
            Set-ADUser -Identity $username -Manager $Manager -Credential $credential -ErrorAction Stop
        }

        Write-Host "User $username created successfully."
        Add-Content -Path $Log_File -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - User $username created successfully."
    } catch {
        # Log error when creating user
        $errorMessage = "Error creating user $username: $_"
        Write-Host $errorMessage
        Add-Content -Path $Log_File -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - $errorMessage"
    }
}

# Stop transcript
Stop-Transcript
