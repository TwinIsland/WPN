# WPN
update the Shadowsocks to get the free VPN

## Usage
1. run `wpn.py`
2. run `WPN.lnk`
3. done

## Config
> all the config stuffs are in `version` file
```json
{
  "update": "2019616", 
  "desc": "first version",
  "source": [ //useless notation
    "github"
  ],
  "checkUpdate": 1,  //whether check update information
  "checkUsable":1, //whether check if ss Account can be used
  "checkDeep":10  // check depth
}
```
## Add new source
put the main crawler function in `source` fold, and modified the `config.py` to merge the `ssAccount` list

## Open Source
**Author:** [Wyatt](https://overfit.org) 

**License:** MIT