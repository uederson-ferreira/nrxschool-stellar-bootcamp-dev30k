pub struct Calculadora {
    last_calc: f64,        // Armazena o último cálculo
    last_op: String,       // Armazena o tipo da última operação
}

impl Calculadora {
    // Cria uma nova calculadora
    pub fn new() -> Self {
        Calculadora {
            last_calc: 0.0,
            last_op: String::new(),
        }
    }

    // Funções para operações matemáticas
    pub fn soma(&mut self, x: f64, y: f64) -> f64 {
        let resultado = x + y;
        self.last_calc = resultado;
        self.last_op = String::from("Soma");
        resultado
    }

    pub fn subtracao(&mut self, x: f64, y: f64) -> f64 {
        let resultado = x - y;
        self.last_calc = resultado;
        self.last_op = String::from("Subtração");
        resultado
    }

    pub fn multiplicacao(&mut self, x: f64, y: f64) -> f64 {
        let resultado = x * y;
        self.last_calc = resultado;
        self.last_op = String::from("Multiplicação");
        resultado
    }

    pub fn divisao(&mut self, x: f64, y: f64) -> Result<f64, &'static str> {
        if y == 0.0 {
            Err("Erro: Divisão por zero não permitida")
        } else {
            let resultado = x / y;
            self.last_calc = resultado;
            self.last_op = String::from("Divisão");
            Ok(resultado)
        }
    }

    // Recupera o tipo e o resultado do último cálculo realizado
    pub fn last_calc(&self) -> (&str, f64) {
        (&self.last_op, self.last_calc)
    }
}
