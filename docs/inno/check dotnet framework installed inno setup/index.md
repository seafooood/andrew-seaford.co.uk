---
title: "Check DotNet Framework is installed during Inno Setup"
date: 2015-02-23
categories: 
  - "inno"
slug: "check-dotnet-framework-installed-inno-setup"
---

To check that DotNet framework is installed during an Inno install. Add the following code section to the install script.

`; Check if dot net is insalled [code] function FrameworkIsNotInstalled: Boolean; begin Result := not RegKeyExists(HKEY_LOCAL_MACHINE, 'Software\Microsoft\.NETFramework\policy\v4.0'); end;  // Install dot net with feedback [Code] procedure InstallFramework; var StatusText: string; ResultCode: Integer; begin StatusText := WizardForm.StatusLabel.Caption; WizardForm.StatusLabel.Caption := 'Installing .NET framework...'; WizardForm.ProgressGauge.Style := npbstMarquee; try if not Exec(ExpandConstant('{tmp}\dotNetFx40_Full_x86_x64.exe'), '/q /noreboot', '', SW_SHOW, ewWaitUntilTerminated, ResultCode) then begin // you can interact with the user that the installation failed MsgBox('.NET installation failed with code: ' + IntToStr(ResultCode) + '.', mbError, MB_OK); end; finally WizardForm.StatusLabel.Caption := StatusText; WizardForm.ProgressGauge.Style := npbstNormal; end; end;`

In the files section add the dotnet installer file. Note the flags AfterInstall and Check that will call the functions to check if DotNet is installed and instal if required.

`Source: "C:\Example\dotNetFx40_Full_x86_x64.exe"; DestDir: {tmp}; Flags: deleteafterinstall; AfterInstall: InstallFramework; Check: FrameworkIsNotInstalled`

Download the installer script [**CheckDotNet.iss**](http://andrew-seaford.co.uk/code/CheckDotNet.iss "CheckDotNet.iss")
