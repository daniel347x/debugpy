import sys
import ptvsd
ptvsd.enable_attach((sys.argv[1], sys.argv[2]))
ptvsd.wait_for_attach()

sys.stdout.write('yes')
sys.stderr.write('no')
