# jselect

jselect is a simple tool to select elements from JSON files.


### Installation
```git clone https://github.com/seemuch/jselect;cd jselect;make```


### Usage
Two usages:
1. jselect file_name wanted_elements  e.g. jselect student.json department.major
2. some_input | jselect wanted_elements  e.g. cat student.json | jselect department.major

### Example
Assume there is a file called sample.json, which looks like the following:
```
{
  "menu": {
    "id": "file",
    "value": "File",
    "popup": {
      "menuitem": [
        {
          "value": "item1",
          "onclick": "itemSelected(1)"
        },
        {
          "value": "item2",
          "onclick": "itemSelected(2)"
        },
        {
          "value": "item3",
          "onclick": "itemSelected(3)"
        }
      ]
    }
  }
}
```

And when you execute the this command:
```jselect manu.json menu.popup.menuitem.value```

The following will be returned:
```
item1
item2
item3
```
