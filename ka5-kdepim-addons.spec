%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kdepim-addons
Summary:	kdepim addons
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c3b5590b75ecc8b005f89efa9f850777
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
BuildRequires:	ka5-akonadi-calendar-devel >= 18.12.0
BuildRequires:	ka5-akonadi-contacts-devel >= 18.12.0
BuildRequires:	ka5-akonadi-devel >= 18.12.0
BuildRequires:	ka5-akonadi-notes-devel >= 18.12.0
BuildRequires:	ka5-calendarsupport-devel >= 18.12.0
BuildRequires:	ka5-eventviews-devel >= 18.12.0
BuildRequires:	ka5-grantleetheme-devel >= 18.12.0
BuildRequires:	ka5-incidenceeditor-devel >= 18.12.0
BuildRequires:	ka5-kcalutils-devel >= 18.12.0
BuildRequires:	ka5-kdepim-apps-libs-devel >= 18.12.0
BuildRequires:	ka5-kidentitymanagement-devel
BuildRequires:	ka5-kimap-devel >= 18.12.0
BuildRequires:	ka5-kitinerary-devel >= 18.12.0
BuildRequires:	ka5-kmailtransport-devel >= 18.12.0
BuildRequires:	ka5-kpimtextedit-devel >= 18.12.0
BuildRequires:	ka5-kpkpass-devel >= 18.12.0
BuildRequires:	ka5-ktnef-devel >= 18.12.0
BuildRequires:	ka5-libgravatar-devel >= 18.12.0
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	ka5-libkleo-devel >= 18.12.0
BuildRequires:	ka5-libksieve-devel >= 18.12.0
BuildRequires:	ka5-mailcommon-devel >= 18.12.0
BuildRequires:	ka5-mailimporter-devel >= 18.12.0
BuildRequires:	ka5-messagelib-devel >= 18.12.0
BuildRequires:	ka5-pimcommon-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdeclarative-devel >= 5.51.0
BuildRequires:	kf5-kholidays-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kparts-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
BuildRequires:	kf5-prison-devel >= 5.51.0
BuildRequires:	kf5-syntax-highlighting-devel >= 5.51.0
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kdepim-addons.categories
/etc/xdg/kdepim-addons.renamecategories
/etc/xdg/kmail.antispamrc
/etc/xdg/kmail.antivirusrc
%attr(755,root,root) %{_bindir}/akonadimailreader
%attr(755,root,root) %{_bindir}/coisceim
%attr(755,root,root) %{_bindir}/etm_usage
%attr(755,root,root) %{_bindir}/kmail_antivir.sh
%attr(755,root,root) %{_bindir}/kmail_clamav.sh
%attr(755,root,root) %{_bindir}/kmail_fprot.sh
%attr(755,root,root) %{_bindir}/kmail_sav.sh
%dir %{_libdir}/contacteditor
%dir %{_libdir}/contacteditor/editorpageplugins
%attr(755,root,root) %{_libdir}/contacteditor/editorpageplugins/cryptopageplugin.so
%attr(755,root,root) %ghost %{_libdir}/libadblocklibprivate.so.5
%attr(755,root,root) %{_libdir}/libadblocklibprivate.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libcoisceim_widget.so.5
%attr(755,root,root) %{_libdir}/libcoisceim_widget.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libkaddressbookimportexportlibprivate.so.5
%attr(755,root,root) %{_libdir}/libkaddressbookimportexportlibprivate.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libkaddressbookmergelibprivate.so.5
%attr(755,root,root) %{_libdir}/libkaddressbookmergelibprivate.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libshorturlpluginprivate.so.5
%attr(755,root,root) %{_libdir}/libshorturlpluginprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/coisceimpart.so
%dir %{_libdir}/qt5/plugins/contacteditor
%attr(755,root,root) %{_libdir}/qt5/plugins/contacteditor/addresslocationeditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/evolutionv1importerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/evolutionv2importerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/gearyimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/nylasmailimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/operaimporterplugin.so
%dir %{_libdir}/qt5/plugins/kaddressbook
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_checkgravatarplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_importexportcsvplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_importexportgmxplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_importexportldapplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_importexportldifplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_importexportvcardplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_mergecontactsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_searchduplicatesplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_sendmailplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook/kaddressbook_sendvcardsplugin.so
%dir %{_libdir}/qt5/plugins/kmail
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_antispamplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_antivirusplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_autocorrectioneditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_automaticaddcontactseditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_changecaseeditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_checkbeforesendeditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_confirmaddresseditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_expertplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_externalcomposereditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_insertemaileditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_insertshorturleditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_insertspecialcharactereditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_logactivitiesplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_nonbreakingspaceeditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_sharetexteditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmail/kmail_zoomtexteditorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/korg_datenums.so
%attr(755,root,root) %{_libdir}/qt5/plugins/korg_picoftheday.so
%attr(755,root,root) %{_libdir}/qt5/plugins/korg_thisdayinhistory.so
%dir %{_libdir}/qt5/plugins/libksieve
%attr(755,root,root) %{_libdir}/qt5/plugins/libksieve/emaillineeditplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libksieve/imapfoldercompletionplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libksieve/regexpeditorlineeditplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/mailtransport/mailtransport_sendplugin.so
%dir %{_libdir}/qt5/plugins/messageviewer/bodypartformatter
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_gnupgwks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_application_mstnef.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_pkpass.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_semantic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_calendar.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_highlighter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/bodypartformatter/messageviewer_bodypartformatter_text_vcard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/grantlee/5.0/kitinerary_grantlee_extension.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_briefheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_createeventplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_createnoteplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_createtodoplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_expandurlplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_externalscriptplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_fancyheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_grantleeheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_longheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_standardsheaderstyleplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/messageviewer/messageviewer_translatorplugin.so
%dir %{_libdir}/qt5/plugins/pimcommon
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/pimcommon_isgdshorturlengineplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/pimcommon_tinyurlengineplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/pimcommon_translatorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pimcommon/pimcommon_triopabshorturlengineplugin.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents
%attr(755,root,root) %{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%dir %{_libdir}/qt5/plugins/templateparser
%attr(755,root,root) %{_libdir}/qt5/plugins/templateparser/templateparseraddressrequesterplugin.so
%dir %{_libdir}/qt5/plugins/webengineviewer
%attr(755,root,root) %{_libdir}/qt5/plugins/webengineviewer/webengineviewer_adblockplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webengineviewer/webengineviewer_donottrackplugin.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/PimCalendars
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/qmldir
%{_desktopdir}/org.kde.akonadimailreader.desktop
%{_datadir}/config.kcfg/mailreader.kcfg
%{_datadir}/contacteditor
%{_datadir}/kconf_update/webengineurlinterceptoradblock.upd
%{_datadir}/kmail2
%{_datadir}/kservices5/coisceimpart.desktop
%dir %{_datadir}/kservices5/korganizer
%{_datadir}/kservices5/korganizer/datenums.desktop
%{_datadir}/kservices5/korganizer/picoftheday.desktop
%{_datadir}/kservices5/korganizer/thisdayinhistory.desktop
%{_datadir}/kxmlgui5/akonadimailreader
%{_datadir}/messageviewer/themes
%dir %{_datadir}/messageviewerplugins
%{_datadir}/messageviewerplugins/externalscriptexample.desktop
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
