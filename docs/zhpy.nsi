; zhpy.nsi
;
;
; How to create an installer for zhpy using this script:
;	1. Install NSIS 2.03(from http://www.nullsoft.com)
;	2. Download Nsisunz (from http://nsis.sourceforge.net/Nsisunz_plug-in ) and put 
;      nsisunz.dll into NSIS/plugins folder.
;	3. Right-click on the zhpy.nsi file and choose "Compile"
;

XPStyle on

;--------------------------------
!define PRODUCT_VERSION "1.0"

!define PRODUCT_NAME "zhpy"
!define PRODUCT_PUBLISHER "Fred Lin"
!define PRODUCT_WEB_SITE "http://code.google.com/p/zhpy"

; The name of the installer
Name "zhpy ${PRODUCT_VERSION}"

; The file to write
OutFile "${PRODUCT_NAME}-${PRODUCT_VERSION}-installer.exe"
LoadLanguageFile "${NSISDIR}\Contrib\Language files\English.nlf"
; The default installation directory
InstallDir $DESKTOP\${PRODUCT_NAME}temp
DirText "Install Assistant will download $(^Name) in the following folder.$\r$\n$\r$\nTo download in a different folder, click Browse and select another folder."
InstallButtonText "Download"

ShowInstDetails show

;--------------------------------

!define STRING_PYTHON_NOT_FOUND "Python is not installed on this system. $\nPlease install Python first. $\n$\nClick OK to download python"
!define STRING_PYTHON_CURRENT_USER_FOUND "Python is installed for the current user only. $\n$\n${PRODUCT_NAME} does not support use with Python so configured. $\n$\nClick OK to cancel installation and remove installation Files."

; Refer to leo's python detection code
; Location where the Installer finds a Pythonw.exe
; set by the .onInit function
var PythonExecutable
var StrNoUsablePythonFound

Function .onInit
	ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Classes\Python.NoConFile\shell\open\command" ""
	StrCpy $8 $9 -8
	IfFileExists $8 ok tryagain
	tryagain:
	    StrCpy $8 $9 -3
	IfFileExists $8 ok tryMSIformat
	tryMSIformat:
	    # is the first character a "
	    StrCpy $8 $9 1
	    StrCmp $8 '"' foundQuote tryMSIformatCurrentUser

	    foundQuote:
	    # OK. Strip off the " at the start as well as the 9 characters at the end
	    StrCpy $8 $9 -9 1
	IfFileExists $8 ok tryMSIformatCurrentUser
	tryMSIformatCurrentUser:
	    ReadRegStr $9 HKEY_CURRENT_USER "SOFTWARE\Classes\Python.NoConFile\shell\open\command" ""

	    # repeating the logic of tryMSIformat:
	    # is the first character a "
	    StrCpy $8 $9 1
	    StrCmp $8 '"' foundQuoteCurrentUser oops

	    # Patch: 10/6/06: Complain if Python not found.
	    StrCmp $8 '"' foundQuoteCurrentUser 0
	    StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"
	    Goto oops

	    foundQuoteCurrentUser:
	    # OK. Strip off the " at the start as well as the 9 characters at the end
	    StrCpy $8 $9 -9 1

	    !ifdef INSTALL_IF_PYTHON_FOR_CURRENT_USER
	      StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"
	      IfFileExists $8 ok oops
	    !else
	      IfFileExists $8 usePythonCUFoundMessage usePythonNotFoundMessage
	      usePythonCUFoundMessage:
	      StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_CURRENT_USER_FOUND}"
	      goto oops
	      usePythonNotFoundMessage:
	      StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"
	      goto oops
	    !endif
	oops:
	    MessageBox MB_OK "$StrNoUsablePythonFound"
	    ;Quit
		Call DownloadPython
		MessageBox MB_OK "Python was downloaded.\nClick OK to install Python"
		Call InstallPython
	ok:
	    MessageBox MB_OK "Found Python executable at '$8'"
	    StrCpy $PythonExecutable $8
FunctionEnd
;--------------------------------

; Pages

Page directory
Page instfiles

Var remote_file
Var local_file
 
;--------------------------------

; The stuff to install
Section "DownloadZhpy" ;No components page, name is not important

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Download file
  ; Call DownloadPython
  Call DownloadZhpy
  Call InstallZhpy
  ; Put file there
  ; File example1.nsi
  
SectionEnd ; end the section

Function DownloadPython
    StrCpy $remote_file "http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi"
	StrCpy $local_file "${PRODUCT_NAME}-${PRODUCT_VERSION}.zip"
	Call DownloadFile
FunctionEnd

Function InstallPython
	Exec '"$INSTDIR\python-2.5.1.msi"'
	ExpandEnvStrings $0 "Path=%Path%;c:\python25;c:\python25\Scripts;"
FunctionEnd

Function DownloadZhpy
    StrCpy $remote_file "http://zhpy.googlecode.com/files/${PRODUCT_NAME}-${PRODUCT_VERSION}.zip"
	StrCpy $local_file "${PRODUCT_NAME}-${PRODUCT_VERSION}.zip"
	Call DownloadFile
	;Call UnzipFile
FunctionEnd

Function InstallZhpy
	Call UnzipFile
	ExecScript "cd $INSTDIR\${PRODUCT_NAME}-${PRODUCT_VERSION}"
	ExecScript "python setup.py install"
FunctionEnd

Function DownloadFile
    NSISdl::download $remote_file "$INSTDIR\$local_file"
	Pop $R0 ; Get the return value
	StrCmp $R0 "success" download_ok
	    SetDetailsView show
		DetailPrint "下載 $R0 失敗"
		Abort
	download_ok:
	    DetailPrint "下載 $R0 完成"
FunctionEnd

Function UnzipFile
    DetailPrint " 解壓縮 $R0..."
	nsisunz::UnzipToLog "$INSTDIR\$local_file" "$INSTDIR"
    Pop $R0
    StrCmp $R0 "success" unzip_ok
		DetailPrint "失敗"
		Abort
	unzip_ok:
	    DetailPrint "完成"
		;Delete "$INSTDIR\$local_file"
FunctionEnd