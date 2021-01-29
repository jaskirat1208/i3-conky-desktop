#!/usr/bin/python3

import subprocess

tmp = subprocess.getoutput("/usr/lib/update-notifier/apt-check")

# Results are like "10;1" so we split them
updates, security = [int(s) for s in tmp.split(';')]

# Change colours for warnings
if updates > 100:
    u_color = 'red'
elif updates > 0:
    u_color = 'green'
else:
    u_color = 'grey'

if security > 0:
    s_color = 'red'
else:
    s_color = 'grey'

u_color = '${color ' + u_color + '}'
s_color = '${color ' + s_color + '}'
end_color = '${color}'

print('  {0}{1}{2} updates'.format(u_color, updates, end_color))
print('  {0}{1}{2} security updates'.format(s_color, security, end_color))
