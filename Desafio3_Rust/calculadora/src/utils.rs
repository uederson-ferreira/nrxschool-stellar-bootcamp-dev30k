use std::io::{self, Write};

// Função para ler entrada do usuário e converter para f64
pub fn ler_numero() -> f64 {
    let mut entrada = String::new();
    io::stdin()
        .read_line(&mut entrada)
        .expect("Falha ao ler a linha");
    entrada.trim().parse().expect("Por favor, digite um núme