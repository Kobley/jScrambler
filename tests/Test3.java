public class Main {

    public static void main(String[] args) {
        System.out.println("Starting the main method...");

        // Instantiate the outer class
        OuterClass outer = new OuterClass();
        outer.outerMethod();

        // Instantiate and use InnerClass1
        OuterClass.InnerClass1 inner1 = outer.new InnerClass1();
        inner1.innerMethod1();

        // Instantiate and use InnerClass2
        OuterClass.InnerClass2 inner2 = new OuterClass.InnerClass2();
        inner2.innerMethod2();

        // Instantiate and use StaticInnerClass
        StaticInnerClass staticInner = new StaticInnerClass();
        staticInner.staticInnerMethod();
        
        System.out.println("Main method finished.");
    }

    static class StaticInnerClass {
        void staticInnerMethod() {
            System.out.println("Static inner class method.");
            // Call another static method
            staticMethod();
        }

        static void staticMethod() {
            System.out.println("Static method called from static inner class.");
        }
    }

    static class OuterClass {
        void outerMethod() {
            System.out.println("Outer class method.");
            InnerClass1 inner1 = new InnerClass1();
            inner1.innerMethod1();
        }

        class InnerClass1 {
            void innerMethod1() {
                System.out.println("Inner class 1 method.");
                InnerClass2 inner2 = new InnerClass2();
                inner2.innerMethod2();
            }
        }

        static class InnerClass2 {
            void innerMethod2() {
                System.out.println("Inner class 2 method.");
            }
        }
    }
}

