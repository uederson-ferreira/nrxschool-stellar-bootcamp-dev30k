use std::io::{self, Write};

// Função para ler entrada do usuário e converter para f64
pub fn ler_numero() -> f64 {
    let mut entrada = String::new();
    io::stdin()
        .read_line(&mut entrada)
        .expect("Falha ao ler a linha");
    entrada.trim().parse().expect("Por favor, digite um número válido")
}

// Função para limpar a tela
pub fn limpar_tela() {
    // Para sistemas Unix (Linux/Mac), usa o comando `clear`
    // Para Windows, usa o comando `cls`
    if cfg!(target_os = "windows") {
        std::process::Command::new("cls").status().unwrap();
    } else {
        std::process::Command::new("clear").status().unwrap();
    }
}
