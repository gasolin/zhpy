; zhpy.nsi
;
;
; How to create an installer for zhpy using this script:
;	1. Install NSIS 2.03(from http://www.nullsoft.com)
;	2. Download Nsisunz (from http://nsis.sourceforge.net/Nsisunz_plug-in ) and put 
;      nsisunz.dll into NSIS/plugins folder.
;	3. Right-click on the zhpy.nsi file and choose "Compile"
;

;--------------------------------
!define PRODUCT_VERSION "1.0"

!define PRODUCT_NAME "zhpy"
!define PRODUCT_PUBLISHER "Fred Lin"
!define PRODUCT_WEB_SITE "http://code.google.com/p/zhpy"
!define BUILD "46"

XPStyle on
SetCompressor lzma

!include "MUI.nsh"
!include "Sections.nsh"
!include "StrFunc.nsh"

!define MUI_WELCOMEPAGE ;
!define MUI_COMPONENTSPAGE ;
!define MUI_DIRECTORYPAGE ;
;!define MUI_INSTFILESPAGE ;instfiles
!define MUI_ABORTWARNING "Are you sure you want to quit ${PRODUCT_NAME} ${PRODUCT_VERSION}?"
!define MUI_FINISHPAGE ;

; MUI Settings
!define MUI_HEADERIMAGE
; !define MUI_HEADERIMAGE_BITMAP "zhpy.bmp" ; optional
!define MUI_COMPONENTSPAGE_SMALLDESC

; Welcome page
!define MUI_WELCOMEPAGE_TITLE "Welcome to ${PRODUCT_NAME}\r\nVersion ${PRODUCT_VERSION}"
!define MUI_WELCOMEPAGE_TEXT "${PRODUCT_NAME} automates the process of downloading, installing python and zhpy Components.\r\n\nClick Next to continue."
!insertmacro MUI_PAGE_WELCOME

var ChooseMessage
 
; Components page
!define MUI_PAGE_HEADER_SUBTEXT $ChooseMessage
!define MUI_PAGE_CUSTOMFUNCTION_PRE AbortComponents
!insertmacro MUI_PAGE_COMPONENTS

; Directory page
!define MUI_PAGE_HEADER_SUBTEXT "Choose the folder in which to install zhpy."
!define MUI_DIRECTORYPAGE_TEXT_TOP "${PRODUCT_NAME} will install zhpy components in the following directory. To install in a different folder click Browse and select another folder. Click Next to continue."
!define MUI_PAGE_CUSTOMFUNCTION_PRE AbortPage
!insertmacro MUI_PAGE_DIRECTORY

; Install page
!define MUI_PAGE_HEADER_SUBTEXT "Install zhpy"
!define MUI_INSTFILESPAGE_ABORTHEADER_TEXT "Installation Aborted"
!define MUI_INSTFILESPAGE_ABORTHEADER_SUBTEXT "The installation was not completed successfully."
!insertmacro MUI_PAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "SimpChinese"
!insertmacro MUI_LANGUAGE "TradChinese"
!insertmacro MUI_RESERVEFILE_LANGDLL

; MUI end ------
   
;--------------------------------

; The name of the installer
Name "zhpy ${PRODUCT_VERSION}"

; The file to write
OutFile "${PRODUCT_NAME}-${PRODUCT_VERSION}-installer${BUILD}.exe"

; The default installation directory
InstallDir $DESKTOP\${PRODUCT_NAME}temp

DirText "Install Assistant will download $(^Name) to the following folder.$\r$\nClick 'Download' button to start the procedure.$\r$\n$\r$\nTo download in a different folder, click Browse and select another folder."
InstallButtonText "Download"


;--------------------------------

Section "Python 2.5.1" SecPython
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Download python
  ;Call DownloadPython
  ;MessageBox MB_OK "Python was downloaded.$\r$\nClick OK to install Python"
  ;Call InstallPython
  
SectionEnd ; end the section

Section "Zhpy 1.0" SecZhpy
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Download zhpy
  ;Call DownloadZhpy
  ;Call InstallZhpy
SectionEnd ; end the section

; Section descriptions

!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
!insertmacro MUI_DESCRIPTION_TEXT ${SecPython} "Python"
!insertmacro MUI_DESCRIPTION_TEXT ${SecZhpy} "zhpy"
!insertmacro MUI_FUNCTION_DESCRIPTION_END


;--------------------------------

Function .onInit
    StrCpy $ChooseMessage "Choose the zhpy components you would like to install."
    
    !insertmacro MUI_LANGDLL_DISPLAY

	LangDLL::LangDialog "Installer Language" "Please select a language."

	Pop $LANGUAGE
	StrCmp $LANGUAGE "cancel" 0 +2
	Abort

FunctionEnd

Function .onInstSuccess
FunctionEnd

;--------------------------------
; Pages

Page components
Page directory
Page instfiles

Var remote_file
Var local_file

;--------------------------------
; Custom functions

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

;--------------------------------

!define STRING_PYTHON_NOT_FOUND "Python is not installed on this system. $\nPlease install Python first. $\n$\nClick OK to download python"
!define STRING_PYTHON_CURRENT_USER_FOUND "Python is installed for the current user only. $\n$\n${PRODUCT_NAME} does not support use with Python so configured. $\n$\nClick OK to cancel installation and remove installation Files."

; Refer to leo's python detection code
; http://leo.tigris.org/source/browse/leo/dist/leo-4-3.nsi
; Location where the Installer finds a Pythonw.exe
; set by the .onInit function
var PythonExecutable
var StrNoUsablePythonFound

Function DetectPython
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
	    ; MessageBox MB_OK "${STRING_PYTHON_NOT_FOUND}"
	    MessageBox MB_ICONQUESTION|MB_YESNO "${STRING_PYTHON_NOT_FOUND} " IDYES +5
        Abort
	ok:
	    MessageBox MB_OK "Found Python executable at '$8'"
	    StrCpy $PythonExecutable $8
FunctionEnd

ShowInstDetails show

; The stuff to install
Function DownloadPython
    Call DetectPython
    StrCpy $remote_file "http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi"
	StrCpy $local_file "${PRODUCT_NAME}-${PRODUCT_VERSION}.zip"
	Call DownloadFile
FunctionEnd

Function InstallPython
	ExecWait '"$INSTDIR\python-2.5.1.msi"'
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
	Exec 'cd "$INSTDIR\${PRODUCT_NAME}-${PRODUCT_VERSION}"'
	Exec "python setup.py install"
FunctionEnd

;-----------------------------------------------------------------------------------------------------------------------
Function AbortComponents
;-----------------------------------------------------------------------------------------------------------------------
 
    ;IntCmp $Updating 1 +1 ShowPage ShowPage
 
    ;IntCmp $Updates 0 +1 Showpage Showpage
 
    ;StrCpy $FINISH_TEXT "${PRODUCT_NAME} found no updates to install."
    Abort
 
ShowPage:
 
FunctionEnd

;-----------------------------------------------------------------------------------------------------------------------
 Function AbortPage
;-----------------------------------------------------------------------------------------------------------------------
  
   ;IntCmp $Updating 1 +1 TestInstall TestInstall
   Abort

;TestInstall:
   ;IntCmp $Install 1 ShowPage +1 +1
   ;Abort
 
ShowPage:
FunctionEnd