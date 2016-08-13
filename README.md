# orvibo-openhab
A small simple python script, for telling orvibo switches to turn on or off from openhab

## Requirements

Install the python-orvibo module from https://github.com/happyleavesaoc/python-orvibo


## To install

cd /opt/openhab/configuration/scripts #or wherever your openhab is
git clone https://github.com/Br3nda/orvibo-openhab.git

## To configure an open have item
`Switch  ItemName  "Item Description"  <itemicon>  (GroupName)   { exec=">[*:/opt/openhab/configurations/scripts/orvibo/switch.py [IP] %2$s]" }`

For example:
```
Switch  Espresso_Kitchen  "Espresso machine"  <coffeemachine1>  (Kitchen)   { exec=">[*:/opt/openhab/configurations/scripts/orvibo/switch.py 10.1.1.166 %2$s]" }
```

Note: most of the time you only specify the IP of your switch

If you don't know the IP of your orvibo switch, run discover.py to see a list 



