%define		kdeappsver	21.08.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kdepim-addons
Summary:	kdepim addons
Name:		ka5-%{kaname}
Version:	21.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	278d51c3b22db01d214860cf0c81797e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt5-devel >= 1.8.0
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-import-wizard-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-notes-devel >= %{kdeappsver}
BuildRequires:	ka5-calendarsupport-devel >= %{kdeappsver}
BuildRequires:	ka5-eventviews-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-incidenceeditor-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kimap-devel >= %{kdeappsver}
BuildRequires:	ka5-kitinerary-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-kpkpass-devel >= %{kdeappsver}
BuildRequires:	ka5-ktnef-devel >= %{kdeappsver}
BuildRequires:	ka5-libgravatar-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-libksieve-devel >= %{kdeappsver}
BuildRequires:	ka5-mailcommon-devel >= %{kdeappsver}
BuildRequires:	ka5-mailimporter-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-kholidays-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-prison-devel >= %{kframever}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kframever}
BuildRequires:	libmarkdown-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Addons for KDE PIM applications, such as extensions for KMail,
additional themes, and plugins providing extra or advanced
functionality.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kmail.antispamrc
/etc/xdg/kmail.antivirusrc
%attr(755,root,root) %{_bindir}/kmail_antivir.sh
%attr(755,root,root) %{_bindir}/kmail_clamav.sh
%attr(755,root,root) %{_bindir}/kmail_fprot.sh
%attr(755,root,root) %{_bindir}/kmail_sav.sh
%ghost %{_libdir}/libadblocklibprivate.so.5
%attr(755,root,root) %{_libdir}/libadblocklibprivate.so.*.*.*
%ghost %{_libdir}/libkaddressbookmergelibprivate.so.5
%attr(755,root,root) %{_libdir}/libkaddressbookmergelibprivate.so.*.*.*
%ghost %{_libdir}/libshorturlpluginprivate.so.5
%attr(755,root,root) %{_libdir}/libshorturlpluginprivate.so.*.*.*
%ghost %{_libdir}/libgrammarcommon.so.5
%attr(755,root,root) %{_libdir}/libgrammarcommon.so.*.*.*
%ghost %{_libdir}/libkmailgrammalecte.so.5
%attr(755,root,root) %{_libdir}/libkmailgrammalecte.so.*.*.*
%ghost %{_libdir}/libkmaillanguagetool.so.5
%attr(755,root,root) %{_libdir}/libkmaillanguagetool.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/evolutionv1importerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/evolutionv2importerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/gearyimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/nylasmailimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/operaimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/korg_datenums.so
%attr(755,root,root) %{_libdir}/qt5/plugins/korg_picoftheday.so
%attr(755,root,root) %{_libdir}/qt5/plugins/korg_thisdayinhistory.so
%dir %{_libdir}/qt5/plugins/libksieve
%attr(755,root,root) %{_libdir}/qt5/plugins/libksieve/emaillineeditplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libksieve/imapfoldercompletionplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/mailtransport/mailtransport_sendplugin.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents
%attr(755,root,root) %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%dir %{_libdir}/qt5/plugins/templateparser
%attr(755,root,root) %{_libdir}/qt5/plugins/templateparser/templateparseraddressrequesterplugin.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/PimCalendars
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/qmldir
%{_datadir}/kconf_update/webengineurlinterceptoradblock.upd
%dir %{_datadir}/kservices5/korganizer
%{_datadir}/kservices5/korganizer/datenums.desktop
%{_datadir}/kservices5/korganizer/picoftheday.desktop
%{_datadir}/kservices5/korganizer/thisdayinhistory.desktop

%dir %{_libdir}/contacteditor
%dir %{_libdir}/contacteditor/editorpageplugins
%attr(755,root,root) %{_libdir}/contacteditor/editorpageplugins/cryptopageplugin.so
%ghost %{_libdir}/libdkimverifyconfigure.so.5
%attr(755,root,root) %{_libdir}/libdkimverifyconfigure.so.*.*.*
%ghost %{_libdir}/libexpireaccounttrashfolderconfig.so.5
%attr(755,root,root) %{_libdir}/libexpireaccounttrashfolderconfig.so.*.*.*
%ghost %{_libdir}/libfolderconfiguresettings.so.5
%attr(755,root,root) %{_libdir}/libfolderconfiguresettings.so.*.*.*
%ghost %{_libdir}/libkmailmarkdown.so.5
%attr(755,root,root) %{_libdir}/libkmailmarkdown.so.*.*.*
%ghost %{_libdir}/libkmailquicktextpluginprivate.so.5
%attr(755,root,root) %{_libdir}/libkmailquicktextpluginprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/emailaddressselectionldapdialogplugin.so
%dir %{_libdir}/qt5/plugins/kaddressbook
%dir %{_libdir}/qt5/plugins/kaddressbook/importexportplugin
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/importexportplugin/kaddressbook_importexportcsvplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/importexportplugin/kaddressbook_importexportgmxplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/importexportplugin/kaddressbook_importexportldapplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/importexportplugin/kaddressbook_importexportldifplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/importexportplugin/kaddressbook_importexportvcardplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/importexportplugin/kaddressbook_importexportwindowscontactplugin.so
%dir %{_libdir}/qt5/plugins/kaddressbook/mainview
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_checkgravatarplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_mergecontactsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_searchduplicatesplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_sendmailplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_sendvcardsplugin.so
%dir %{_libdir}/qt5/plugins/kmail
%dir %{_libdir}/qt5/plugins/kmail/mainview
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/mainview/kmail_antispamplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/mainview/kmail_antivirusplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/mainview/kmail_expertplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/mainview/kmail_logactivitiesplugin.so
%dir %{_libdir}/qt5/plugins/kmail/plugincheckbeforesend
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugincheckbeforesend/kmail_automaticaddcontactseditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugincheckbeforesend/kmail_checkbeforesendeditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugincheckbeforesend/kmail_confirmaddresseditorplugin.so
%dir %{_libdir}/qt5/plugins/kmail/plugineditor
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_autocorrectioneditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_changecaseeditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_insertemaileditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_insertshorturleditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_insertspecialcharactereditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_nonbreakingspaceeditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_quicktextplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_sharetexteditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditor/kmail_zoomtexteditorplugin.so
%dir %{_libdir}/qt5/plugins/kmail/plugineditorconverttext
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditorconverttext/kmail_markdownplugin.so
%dir %{_libdir}/qt5/plugins/kmail/plugineditorgrammar
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditorgrammar/kmail_grammalecteplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditorgrammar/kmail_languagetoolplugin.so
%dir %{_libdir}/qt5/plugins/kmail/plugineditorinit
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/plugineditorinit/kmail_externalcomposereditorplugin.so
%dir %{_libdir}/qt5/plugins/messageviewer
%dir %{_libdir}/qt5/plugins/messageviewer/bodypartformatter
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_gnupgwks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_mstnef.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_pkpass.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_semantic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_calendar.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_highlighter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_markdown.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_vcard.so
%dir %{_libdir}/qt5/plugins/messageviewer/configuresettings
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/configuresettings/messageviewer_dkimconfigplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/configuresettings/messageviewer_expireaccounttrashfolderconfigplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/configuresettings/messageviewer_folderconfiguresettingsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/configuresettings/messageviewer_gravatarconfigplugin.so
%dir %{_libdir}/qt5/plugins/messageviewer/grantlee
%dir %{_libdir}/qt5/plugins/messageviewer/grantlee/5.0
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/grantlee/5.0/kitinerary_grantlee_extension.so
%dir %{_libdir}/qt5/plugins/messageviewer/headerstyle
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/headerstyle/messageviewer_briefheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/headerstyle/messageviewer_fancyheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/headerstyle/messageviewer_grantleeheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/headerstyle/messageviewer_longheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/headerstyle/messageviewer_standardsheaderstyleplugin.so
%dir %{_libdir}/qt5/plugins/messageviewer/viewercommonplugin
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/viewercommonplugin/messageviewer_expandurlplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/viewercommonplugin/messageviewer_translatorplugin.so
%dir %{_libdir}/qt5/plugins/messageviewer/viewerplugin
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/viewerplugin/messageviewer_createeventplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/viewerplugin/messageviewer_createnoteplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/viewerplugin/messageviewer_createtodoplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/viewerplugin/messageviewer_externalscriptplugin.so
%dir %{_libdir}/qt5/plugins/pimcommon
%dir %{_libdir}/qt5/plugins/pimcommon/customtools
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/customtools/pimcommon_translatorplugin.so
%dir %{_libdir}/qt5/plugins/pimcommon/shorturlengine
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/shorturlengine/pimcommon_isgdshorturlengineplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/shorturlengine/pimcommon_tinyurlengineplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/shorturlengine/pimcommon_triopabshorturlengineplugin.so
%dir %{_libdir}/qt5/plugins/webengineviewer
%dir %{_libdir}/qt5/plugins/webengineviewer/urlinterceptor
%attr(755,root,root) %{_libdir}/qt5/plugins/webengineviewer/urlinterceptor/webengineviewer_adblockplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webengineviewer/urlinterceptor/webengineviewer_donottrackplugin.so
%{_datadir}/kconf_update/languagetool_kmail.upd
%{_datadir}/qlogging-categories5/kdepim-addons.categories
%{_datadir}/qlogging-categories5/kdepim-addons.renamecategories
%ghost %{_libdir}/libkmailconfirmbeforedeleting.so.5
%{_libdir}/libkmailconfirmbeforedeleting.so.5.*.*
%dir %{_libdir}/qt5/plugins/messageviewer/checkbeforedeleting
%{_libdir}/qt5/plugins/messageviewer/checkbeforedeleting/kmail_confirmbeforedeletingplugin.so

#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/CMakeLists.txt
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugin.json.impl
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.cpp
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.h
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.cpp
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.h
#%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins/wizard.json
#%{_datadir}/qtcreator/templates/kmaileditorplugins/CMakeLists.txt
#%{_datadir}/qtcreator/templates/kmaileditorplugins/plugin.json.impl
#%{_datadir}/qtcreator/templates/kmaileditorplugins/plugineditor.cpp
#%{_datadir}/qtcreator/templates/kmaileditorplugins/plugineditor.h
#%{_datadir}/qtcreator/templates/kmaileditorplugins/plugineditorinterface.cpp
#%{_datadir}/qtcreator/templates/kmaileditorplugins/plugineditorinterface.h
#%{_datadir}/qtcreator/templates/kmaileditorplugins/wizard.json
