#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kdepim-addons
Summary:	kdepim addons
Name:		ka5-%{kaname}
Version:	23.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	53e4dec992d1d498fedf25c6f9581ed3
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
BuildRequires:	ka5-kaddressbook-devel >= %{kdeappsver}
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
ExcludeArch:	x32
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
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


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
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents
%attr(755,root,root) %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%dir %{_libdir}/qt5/qml/org/kde/plasma/PimCalendars
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/qmldir
%{_datadir}/kconf_update/webengineurlinterceptoradblock.upd

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
%{_datadir}/qlogging-categories5/kdepim-addons.categories
%{_datadir}/qlogging-categories5/kdepim-addons.renamecategories
%ghost %{_libdir}/libkmailconfirmbeforedeleting.so.5
%attr(755,root,root) %{_libdir}/libkmailconfirmbeforedeleting.so.5.*.*
%ghost %{_libdir}/libscamconfiguresettings.so.5
%attr(755,root,root) %{_libdir}/libscamconfiguresettings.so.5.*.*
%{_iconsdir}/hicolor/scalable/status/moon-phase-first-quarter.svg
%{_iconsdir}/hicolor/scalable/status/moon-phase-full.svg
%{_iconsdir}/hicolor/scalable/status/moon-phase-last-quarter.svg
%{_iconsdir}/hicolor/scalable/status/moon-phase-new.svg
%ghost %{_libdir}/libopenurlwithconfigure.so.5
%attr(755,root,root) %{_libdir}/libopenurlwithconfigure.so.*.*.*

%ghost %{_libdir}/libakonadidatasetools.so.5
%{_libdir}/libakonadidatasetools.so.*.*.*
%{_libdir}/qt5/plugins/pim5/akonadi/emailaddressselectionldapdialogplugin.so
%dir %{_libdir}/qt5/plugins/pim5/contacteditor
%dir %{_libdir}/qt5/plugins/pim5/contacteditor/editorpageplugins
%{_libdir}/qt5/plugins/pim5/contacteditor/editorpageplugins/cryptopageplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/evolutionv1importerplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/evolutionv2importerplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/gearyimporterplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/operaimporterplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kaddressbook
%dir %{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin
%{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin/kaddressbook_importexportcsvplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin/kaddressbook_importexportgmxplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin/kaddressbook_importexportldapplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin/kaddressbook_importexportldifplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin/kaddressbook_importexportvcardplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin/kaddressbook_importexportwindowscontactplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kaddressbook/mainview
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_checkgravatarplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_mergecontactsplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_searchduplicatesplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_sendmailplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_sendvcardsplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kmail
%dir %{_libdir}/qt5/plugins/pim5/kmail/mainview
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_akonadidatabasetoolplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_antispamplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_antivirusplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_expertplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kmail/plugincheckbeforesend
%{_libdir}/qt5/plugins/pim5/kmail/plugincheckbeforesend/kmail_automaticaddcontactseditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugincheckbeforesend/kmail_checkbeforesendeditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugincheckbeforesend/kmail_confirmaddresseditorplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kmail/plugineditor
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_autocorrectioneditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_changecaseeditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_insertemaileditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_insertshorturleditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_insertspecialcharactereditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_nonbreakingspaceeditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_quicktextplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_sharetexteditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_zoomtexteditorplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kmail/plugineditorconverttext
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorconverttext/kmail_markdownplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kmail/plugineditorgrammar
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorgrammar/kmail_grammalecteplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorgrammar/kmail_languagetoolplugin.so
%dir %{_libdir}/qt5/plugins/pim5/kmail/plugineditorinit
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorinit/kmail_externalcomposereditorplugin.so
%dir %{_libdir}/qt5/plugins/pim5/korganizer
%{_libdir}/qt5/plugins/pim5/korganizer/datenums.so
%{_libdir}/qt5/plugins/pim5/korganizer/lunarphases.so
%{_libdir}/qt5/plugins/pim5/korganizer/picoftheday.so
%{_libdir}/qt5/plugins/pim5/korganizer/thisdayinhistory.so
%dir %{_libdir}/qt5/plugins/pim5/libksieve
%{_libdir}/qt5/plugins/pim5/libksieve/emaillineeditplugin.so
%{_libdir}/qt5/plugins/pim5/libksieve/imapfoldercompletionplugin.so
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_gnupgwks.so
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_mstnef.so
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_pkpass.so
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_semantic.so
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_calendar.so
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_highlighter.so
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_markdown.so
%{_libdir}/qt5/plugins/pim5/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_vcard.so
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/checkbeforedeleting
%{_libdir}/qt5/plugins/pim5/messageviewer/checkbeforedeleting/kmail_confirmbeforedeletingplugin.so
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/configuresettings
%{_libdir}/qt5/plugins/pim5/messageviewer/configuresettings/messageviewer_dkimconfigplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/configuresettings/messageviewer_expireaccounttrashfolderconfigplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/configuresettings/messageviewer_folderconfiguresettingsplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/configuresettings/messageviewer_gravatarconfigplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/configuresettings/messageviewer_openurlwithconfigplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/configuresettings/messageviewer_scamconfiguresettingsplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/grantlee/5.0/kitinerary_grantlee_extension.so
%{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle/messageviewer_briefheaderstyleplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle/messageviewer_fancyheaderstyleplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle/messageviewer_grantleeheaderstyleplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle/messageviewer_longheaderstyleplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/headerstyle/messageviewer_standardsheaderstyleplugin.so
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/viewercommonplugin
%{_libdir}/qt5/plugins/pim5/messageviewer/viewercommonplugin/messageviewer_expandurlplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/viewercommonplugin/messageviewer_translatorplugin.so
%dir %{_libdir}/qt5/plugins/pim5/messageviewer/viewerplugin
%{_libdir}/qt5/plugins/pim5/messageviewer/viewerplugin/messageviewer_createeventplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/viewerplugin/messageviewer_createnoteplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/viewerplugin/messageviewer_createtodoplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer/viewerplugin/messageviewer_externalscriptplugin.so
%dir %{_libdir}/qt5/plugins/pim5/pimcommon
%dir %{_libdir}/qt5/plugins/pim5/pimcommon/customtools
%{_libdir}/qt5/plugins/pim5/pimcommon/customtools/pimcommon_translatorplugin.so
%dir %{_libdir}/qt5/plugins/pim5/pimcommon/shorturlengine
%{_libdir}/qt5/plugins/pim5/pimcommon/shorturlengine/pimcommon_isgdshorturlengineplugin.so
%{_libdir}/qt5/plugins/pim5/pimcommon/shorturlengine/pimcommon_tinyurlengineplugin.so
%{_libdir}/qt5/plugins/pim5/pimcommon/shorturlengine/pimcommon_triopabshorturlengineplugin.so
%dir %{_libdir}/qt5/plugins/pim5/templateparser
%{_libdir}/qt5/plugins/pim5/templateparser/templateparseraddressrequesterplugin.so
%dir %{_libdir}/qt5/plugins/pim5/webengineviewer
%dir %{_libdir}/qt5/plugins/pim5/webengineviewer/urlinterceptor
%{_libdir}/qt5/plugins/pim5/webengineviewer/urlinterceptor/webengineviewer_adblockplugin.so
%{_libdir}/qt5/plugins/pim5/webengineviewer/urlinterceptor/webengineviewer_donottrackplugin.so
%{_libdir}/qt5/plugins/pim5/mailtransport/mailtransport_sendplugin.so


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
