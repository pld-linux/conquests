Summary:	Turn based strategy game similar to Civilization
Summary(hu.UTF-8):	Körökre osztott stratégiai játék, a Civilization-hoz hasonló
Name:		conquests
Version:	0.11
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games/Strategy
Source0:	http://homepage.ntlworld.com/mark.harman/%{name}_src.zip
# Source0-md5:	ca45310a13d91bf9ecfd077fb72132fe
URL:		http://homepage.ntlworld.com/mark.harman/conquests.html
Patch0:		makefile.patch
BuildRequires:	FreeImage-devel
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	cg-devel
BuildRequires:	freetype-devel
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Turn based strategy game similar to Civilization.


%description -l hu.UTF-8
Körökre osztott stratégiai játék, a Civilization-hoz hasonló.

%prep
%setup -q -n %{name}_src
%patch -P0 -p1
%{__sed} -i "s@lua5\.1/@@" conquests/game.h

%build
PACKS="lua51 freetype2 SDL_mixer"
%{__make} -f makefile_conquests \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags}" \
	INC="`pkg-config --cflags $PACKS`" \
	LIBS="`pkg-config --cflags $PACKS` -lfreeimage"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
