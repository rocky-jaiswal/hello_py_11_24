{
  description = "Hello Py -> 11 2024";

  # Flake inputs
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  # Flake outputs
  outputs = { self, nixpkgs }:
    let
      # Systems supported
      allSystems = [
        "x86_64-linux" # 64-bit Intel/AMD Linux
        # "aarch64-linux" # 64-bit ARM Linux
        # "x86_64-darwin" # 64-bit Intel macOS
        # "aarch64-darwin" # 64-bit ARM macOS
      ];

      # Helper to provide system-specific attributes
      forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      # Development environment output
      devShells = forAllSystems ({ pkgs }: {
        default = pkgs.mkShell {
          # The Nix packages provided in the environment
          packages = with pkgs; [
            python3
            ruff
            poetry
            python311Packages.jupyterlab
          ];

          # Environment variables
          env = {
            GREETING = "Hello from Python!";
          };

          # A hook run every time you enter the environment
          shellHook = ''
            echo $GREETING
            python --version
            while IFS= read -r line; do export "$line"; done < .env
          '';
        };
      });
    };
}
