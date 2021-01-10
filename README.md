# Offline markdown toc

Simple python script to generate a table of contents from a markdown file and its headings.

## Table of Contents

**[Example of heading 2](#Example-of-heading-2)**

**[......Example of heading 3](#Example-of-heading-3)**

**[......Example of heading 4](#Example-of-heading-4)**

**[Example of heading 5](#Example-of-heading-5)**

**[......Example of heading 6](#Example-of-heading-6)**

**[........Example of heading 7](#Example-of-heading-7)**

**[Example of heading 8](#Example-of-heading-8)**

**[......Example of heading 9](#Example-of-heading-9)**

**[........Example of heading 10](#Example-of-heading-10)**

**[..........Example of heading 11](#Example-of-heading-11)**

**[............Example of heading 12](#Example-of-heading-12)**

**[Usage](#Usage)**

**[......Optional parameters](#Optional-parameters)**

**[Requirements](#Requirements)**

## Example of heading 2

Nesting of headings is supported

### Example of heading 3

### Example of heading 4

## Example of heading 5

### Example of heading 6

#### Example of heading 7

## Example of heading 8

### Example of heading 9

#### Example of heading 10

##### Example of heading 11

###### Example of heading 12

6 levels of headings are supported

## Usage

Run the following command line example from this folder. It will create the output file based of this readme.

```
python generateTOC.py README.md Output.md
```

### Optional parameters

If -c is passed in, the user can replace the default dot (.) for nested headings. In the example the underscore was used. Note that "space" is automatically removed from link names by some markdown renderers.

```
python generateTOC.py README.md Output.md -c _
```

## Requirements

- Python 3
