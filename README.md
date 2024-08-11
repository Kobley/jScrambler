# jScrambler
 Python script to scramble and encode/encrypt .java files as a preprocessing layer to heavier obfuscation.

## usage
> [!IMPORTANT]
> TODO: option parser for command line usage

## showcase
> ![usage](https://github.com/Kobley/jScrambler/blob/master/media/usage.gif)

```java
public class Test {
  public static void main(String[] args) {
    String msg = getMessage();
    System.out.println(msg);
  }

  public static String getMessage() {
    return "Hello World!";
  }
}
```

## Becomes

```java
public class hTdBJUPaORIOVBGZNgTsfAxgRRcZKXWD {
  public static void main(String[] args) {
    String msg = cfLjVgtFvwvirnBbFBKVShQygtaVvBxdFckHxuVkTHRJfgwBlEytfpwyCKuDcKQC();
    System.out.println(msg);
  }

  public static String cfLjVgtFvwvirnBbFBKVShQygtaVvBxdFckHxuVkTHRJfgwBlEytfpwyCKuDcKQC() {
    return new StringBuilder("!dlroW olleH").reverse().toString();
  }
}
```

## this project is licensed with the GNU GPLv3 license.
> ### below is a summary.

The GNU General Public License version 3 (GPLv3) is a free software license designed to ensure that software remains free and open for all users. It allows anyone to use, study, modify, and distribute the software, provided that any distributed versions, including modified ones, are also licensed under GPLv3, ensuring that derivative works remain free. The license includes protections against patent claims and prohibits the use of hardware restrictions to prevent users from running modified versions of the software. This strong copyleft license ensures that the freedoms granted by the original software are preserved in all copies and derivative works.
