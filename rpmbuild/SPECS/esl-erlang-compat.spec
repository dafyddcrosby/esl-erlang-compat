Name: esl-erlang-compat
Version: R16B03
Release: 1
Summary: A compat file to get esl-erlang to provide erlang
URL:  https://github.com/jasonmcintosh/esl-erlang-compat
License: MPLv1.1 and MIT and ASL 2.0 and BSD
Source0: $_sourcedir/esl-erlang-compat.tar.gz
BuildArch: noarch
Requires: esl-erlang >= R16B03
Provides: erlang
BuildRoot: %{_tmppath}/%{name}-root

%description
A compat file to allow esl-erlang to provide erlang dependencies.  Updated to 16B03 for rabbitmq 3.6.0

%prep
%setup -qn esl-erlang-compat


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/esl-erlang-compat/
cp -p version.txt $RPM_BUILD_ROOT%{_sysconfdir}/esl-erlang-compat/

%files
%defattr(-,root,root)
%{_sysconfdir}/esl-erlang-compat/version.txt

%changelog
* Wed Jul 5 2015 Jason McIntosh <mcintoshj@gmail.com>
- Updated to use R16B03 as minimum version

%clean
rm -rf $RPM_BUILD_ROOT
