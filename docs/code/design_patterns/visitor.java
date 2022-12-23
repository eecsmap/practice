

public class visitor {
    public static void main(String[] args) {
        Visitor visitorA = new VisitorA();
        Visitor visitorB = new VisitorB();
        VisitableA visitableA = new VisitableA();
        VisitableB visitableB = new VisitableB();

        visitableA.accept(visitorA);
        visitableA.accept(visitorB);
        visitableB.accept(visitorA);
        visitableB.accept(visitorB);
    }
}

interface Visitor {

    void visit(VisitableA visitable);
    void visit(VisitableB visitableB);

    class DefaultVisitor implements Visitor {

        void defaultVisit(Visitable visitable) {
            System.out.println("default visit: " + visitable.getClass());
        }

        public void visit(VisitableA visitable) {
            defaultVisit(visitable);
        }

        public void visit(VisitableB visitable) {
            defaultVisit(visitable);
        }
    }
}

class VisitorA extends Visitor.DefaultVisitor {
    public void visit(VisitableA visitable) {
        System.out.println("VisitorA visits " + visitable.getClass());
    }

    public void visit(VisitableB visitable) {
        System.out.println("VisitorA visits " + visitable.getClass());
    }
}

class VisitorB extends Visitor.DefaultVisitor {
    public void visit(VisitableA visitable) {
        System.out.println("VisitorB visits " + visitable.getClass());
    }

    public void visit(VisitableB visitable) {
        System.out.println("VisitorB visits " + visitable.getClass());
    }
}

interface Visitable {
    default void accept(Visitor visitor) {
    }
}

class VisitableA implements Visitable {
    // public void accept(Visitor visitor) {
    //     visitor.visit(this);
    // }
}

class VisitableB implements Visitable {
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}