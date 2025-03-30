# Source code disclosure via backup files

**Lab Url**: [https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files)

![Lab Description](img/lab-description.png)

## Analysis

The initial step is to understand how the vulnerable application works and gather information about the target system. The application contains a **`robots.txt`** file that discloses a hint of the existence of a backup directory.

![Robots](img/robots-txt.png)

After visiting the backup page, I found a link that redirects to `ProductTemplate.java.bak` which typically represents a backup copy of a Java source code file.

![Backup Page](img/backup.png)

You can find the **password** of the `Postgres` database hardcoded in the source code file.

![Db Password](img/db-password.png)

Submit the **password** to solve this lab.

![Lab solved](img/lab-solved.png)
