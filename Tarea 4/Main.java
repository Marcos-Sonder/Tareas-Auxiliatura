class Anuncio {
    private int numero;
    private double precio;

    public Anuncio() {
        this(0, 0.1);
    }

    public Anuncio(int num, double pre) {
        numero = num;
        precio = pre;
    }

    public int getNumero() {
        return numero;
    }

    public double getPrecio() {
        return precio;
    }
}

class Artista {
    private String nombre;
    private int ci;
    private int aniosExp;

    public Artista(String nom, int car, int anios) {
        nombre = nom;
        ci = car;
        aniosExp = anios;
    }

    public String getNombre() {
        return nombre;
    }

    public int getCi() {
        return ci;
    }

    public int getAnios() {
        return aniosExp;
    }
}

class Obra {
    protected String titulo;
    protected String material;
    protected Artista artista1;
    protected Artista artista2;
    protected Anuncio anuncio;

    public Obra(String titulo, String material,
                String nom1, int car1, int anio1,
                String nom2, int car2, int anio2) {
        this.titulo = titulo;
        this.material = material;
        artista1 = new Artista(nom1, car1, anio1);
        artista2 = new Artista(nom2, car2, anio2);
        anuncio = null;
    }

    public void agregarAnuncio(Anuncio anun) {
        anuncio = anun;
    }

    public Anuncio getAnuncio() {
        return anuncio;
    }

    public Artista getArt1() {
        return artista1;
    }

    public Artista getArt2() {
        return artista2;
    }

    public String getTitulo() {
        return titulo;
    }
}

class Pintura extends Obra {
    private String genero;

    public Pintura(String titulo, String material,
                   String nom1, int car1, int anio1,
                   String nom2, int car2, int anio2, String gen) {
        super(titulo, material, nom1, car1, anio1,
              nom2, car2, anio2);
        genero = gen;
    }
}

public class Main {
    // Inciso b
    public static Artista artistaConMasExperiencia(Pintura p1, Pintura p2) {
        Artista[] artistas = {
            p1.getArt1(), p1.getArt2(), p2.getArt1(), p2.getArt2()
        };

        Artista mayor = artistas[0];
        for (Artista artista : artistas) {
            if (artista.getAnios() > mayor.getAnios()) {
                mayor = artista;
            }
        }
        return mayor;
    }

    // Inciso c
    public static double montoTotalVenta(Pintura p1, Pintura p2) {
        double total = 0;
        if (p1.getAnuncio() != null) {
            total += p1.getAnuncio().getPrecio();
        }
        if (p2.getAnuncio() != null) {
            total += p2.getAnuncio().getPrecio();
        }
        return total;
    }

    public static void main(String[] args) {
        // Inciso a
        Anuncio a1 = new Anuncio();
        Anuncio a2 = new Anuncio(2, 2.3);

        Pintura p1 = new Pintura("monalisa", "oleo",
                "davinci", 123, 20, "joel", 321, 1, "intriga");
        Pintura p2 = new Pintura("monalisa", "oleo",
                "davinci", 123, 20, "adrian", 444, 4, "cuatro");

        p2.agregarAnuncio(a1);

        // Inciso b
        Artista artista = artistaConMasExperiencia(p1, p2);
        System.out.println("Artista con mayor experiencia: " + artista.getNombre());
        System.out.println("Anos de experiencia: " + artista.getAnios());

        // Inciso c
        p1.agregarAnuncio(a2);
        System.out.println("Monto total de venta: " + montoTotalVenta(p1, p2));
    }
}
