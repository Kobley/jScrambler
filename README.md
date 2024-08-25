# jScrambler
 Python script to scramble and encode/encrypt .java files as a preprocessing layer to heavier obfuscation.

## usage
> [!IMPORTANT]
> TODO: option parser for command line usage

## showcase
> [!WARNING]
> ### outdated showcase
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
public class YKXs {
  public static void main(String[] args) {
    String msg = USkJGwUp();
    System.out.println(msg);
  }

  public static String USkJGwUp() {
    return new StringBuilder(new StringBuilder((new Object() {
        long t;
        public String toString() {
            byte[] buf = new byte[12];
            t = 805898673L; buf[0] = (byte) (t >>> 13);
            t = 965790588L; buf[1] = (byte) (t >>> 9);
            t = 1922316505L; buf[2] = (byte) (t >>> 1);
            t = 105604781L; buf[3] = (byte) (t >>> 11);
            t = 2958945503L; buf[4] = (byte) (t >>> 1);
            t = 883591298L; buf[5] = (byte) (t >>> 2);
            t = 1501739252L; buf[6] = (byte) (t >>> 11);
            t = 590777828L; buf[7] = (byte) (t >>> 5);
            t = 3104606268L; buf[8] = (byte) (t >>> 23);
            t = 3385691947L; buf[9] = (byte) (t >>> 13);
            t = 4131730282L; buf[10] = (byte) (t >>> 20);
            t = 1645935893L; buf[11] = (byte) (t >>> 20);
            return new String(buf);
        }
    }.toString())).reverse().toString()).reverse().toString();
  }
}
```

## this project is licensed with the GNU GPLv3 license.
> ### below is a summary.

The GNU General Public License version 3 (GPLv3) is a free software license designed to ensure that software remains free and open for all users. It allows anyone to use, study, modify, and distribute the software, provided that any distributed versions, including modified ones, are also licensed under GPLv3, ensuring that derivative works remain free. The license includes protections against patent claims and prohibits the use of hardware restrictions to prevent users from running modified versions of the software. This strong copyleft license ensures that the freedoms granted by the original software are preserved in all copies and derivative works.
