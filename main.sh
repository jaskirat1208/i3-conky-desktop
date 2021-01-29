cd "$1"
conky -c conky-cpu-info.conf &
conky -c conky-update-info.conf &
conky -c conky-username.conf &
conky -c ycomb-rss-info.conf &
fg