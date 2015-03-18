# -*- mode: python -*-
a = Analysis(['RedNoseGenerator.py'],
             pathex=['D:\\'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='RedNoseGenerator.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
