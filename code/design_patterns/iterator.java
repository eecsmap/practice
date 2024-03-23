package docs.code.design_patterns;

public class iterator {
    
}

interface Iterator {
    boolean hasNext();
    Object next();
}

interface Iterable {
    Iterator iterator();
}
