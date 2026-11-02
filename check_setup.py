import sys
print("Python:", sys.version.split()[0])
for name in ("numpy", "pandas", "sklearn", "torch", "matplotlib"):
    try:
        module = __import__(name)
        print(f"{name}: {getattr(module, '__version__', 'installed')}")
    except ImportError:
        print(f"{name}: NOT INSTALLED")
