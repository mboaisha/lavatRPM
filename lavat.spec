Name:       lavat
Version:    3.0.0
Release:    %autorelease
Summary:    Lava lamp simulation using metaballs in the terminal

License:    MIT
URL:        https://github.com/AngelJumbo/%{name}
Source0:    %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

Provides:   bundled(termbox2)

%description
Little program that simulates a lava lamp in the terminal.

%prep
%autosetup -n %{name}-%{version}

%build
%set_build_flags
gcc %{build_cflags} %{build_ldflags} lavat.c -o lavat

%install
install -Dpm 0755 lavat %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
