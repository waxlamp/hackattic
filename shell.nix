with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "d3mlm-ta2-env";
  buildInputs = [
    # System requirements.
    readline

    # Python requirements (enough to get a virtualenv going).
    python27Full
    python27Packages.requests
  ];
  src = null;
  shellHook = ''
    # Allow the use of wheels.
    SOURCE_DATE_EPOCH=$(date +%s)

    # Augment the dynamic linker path
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${readline}/lib
  '';
}
