#!/usr/bin/python3
import netifaces

BOX_HEIGHT = 20
BAR_HEIGHT = 5

WIDTH = 255


class Info:
    key = ''
    value = ''
    curr_usage = ''
    cum_usage = ''

    def __str__(self):
        return str.format('''
            ${{color gold}} {key} ${{color}} : {val}
              {curr_usage}
            {cum_usage}
        ''', key=self.key, val=self.value, curr_usage=self.curr_usage, cum_usage=self.cum_usage)


class CPUInfo(Info):
    def __init__(self):
        self.key = 'CPU'
        self.value = '$freq_g GHz'
        self.curr_usage = str.format('${{cpu}}% ${{cpubar {}, {}}}', BAR_HEIGHT, WIDTH)
        self.cum_usage = str.format('${{cpugraph {},{} 7fff00 ff0000 -t}}', BOX_HEIGHT, WIDTH)


class MemInfo(Info):
    def __init__(self):
        self.key = 'RAM'
        self.value = '${mem} / ${memmax}'
        self.curr_usage = str.format('${{memperc}}% ${{membar {},{}}}', BAR_HEIGHT, WIDTH)
        self.cum_usage = '${memgraph 20,255 7fff00 ff0000 -t}'


class Clock:
    def __init__(self):
        pass

    def __str__(self):
        curr_time_str = '''
            ${voffset 5} $color ${alignc}${font Droid Sans Mono:pixelsize=40}${time %H:%M}${font}
            ${voffset 5} $color ${alignc}${font Droid Sans Mono:pixelsize=15}${time %A %d %B %Y}${font}
        '''
        return curr_time_str


class FileSystem:
    def __init__(self):
        self.width = WIDTH
        self.bar_height = BAR_HEIGHT

    def __str__(self):
        return '''
        ${color gold}File systems:${color}
          ${color gold}/:   ${color}${fs_used /} / ${fs_size /}
        ${fs_bar ''' + f'{self.bar_height},{self.width}' + ''' /}
          ${color gold}/home:   ${color}${fs_used /home} / ${fs_size /home} 
        ${fs_bar ''' + f'{self.bar_height},{self.width}' + ''' /home}
        '''


class NetworkInfo:
    def __init__(self):
        self.interfaces = netifaces.interfaces()

    def __str__(self):
        output = '${color gold}${font :size=12}Network:$font $color'
        for interface in self.interfaces:
            output += '''
                  ${color gold}%s:${color} ${voffset -1}${font :size=9}${color grey}${addrs %s} / ${execpi 300 scripts/get_ip.sh}${color}${font}
                  ${voffset 5}${template1}  ${downspeedf %s} kB/s ${goto 145}${template0} ${upspeedf %s} kB/s
                  ${downspeedgraph %s %s,%s 7fff00 ff0000 -t} ${upspeedgraph %s %s,%s 7fff00 ff0000 -t}
            ''' % (interface, interface, interface, interface, interface, BOX_HEIGHT, WIDTH/2, interface, BOX_HEIGHT, WIDTH/2)

        return output


def hr():
    return '${color dark grey}$hr $color\n'


def main():
    out = str(Clock())
    out += hr()
    out += str(CPUInfo())
    out += hr()
    out += str(MemInfo())
    out += hr()
    out += str(FileSystem())
    out += hr()
    out += str(NetworkInfo())
    print(out.replace('    ', ''))


if __name__ == '__main__':
    main()
