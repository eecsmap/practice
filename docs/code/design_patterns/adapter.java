package docs.code.design_patterns;

public class adapter {
    
    public static void main(String[] args) {
        InterfaceBClient interfaceBClient = new InterfaceBClient();
        InterfaceA adapted = new Adapted();
        InterfaceB adapter = new Adapter(adapted);
        interfaceBClient.methodBClient(adapter);
    }
}

interface InterfaceA {
    void methodA();
}

interface InterfaceB {
    void methodB();
}

class Adapted implements InterfaceA {

    public void methodA() {
        System.out.println("methodA");
    }

}

class InterfaceBClient {

    public void methodBClient(InterfaceB interfaceB) {
        interfaceB.methodB();
    }
}

class Adapter implements InterfaceB {

    private InterfaceA interfaceA;

    public Adapter(InterfaceA interfaceA) {
        this.interfaceA = interfaceA;
    }

    public void methodB() {
        interfaceA.methodA();
    }
}
