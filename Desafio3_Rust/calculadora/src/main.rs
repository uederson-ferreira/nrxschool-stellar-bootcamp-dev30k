mod calculadora;
mod utils;

use calculadora::Calculadora;
use utils::{ler_numero, limpar_tela};

fn main() {
    let mut calc = Calculadora::new();

    loop {
        println!("\nEscolha uma operação:");
        println!("1 - Soma");
        println!("2 - Subtração");
        println!("3 - Multiplicação");
        println!("4 - Divisão");
        println!("5 - Último cálculo");
        println!("6 - Sair");

        let mut escolha = String::new();
        std::io::stdin()
            .read_line(&mut escolha)
            .expect("Falha ao ler a linha");
        let escolha: u32 = match escolha.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        if escolha == 6 {
            limpar_tela();  // Limpa a tela antes de mostrar o último cálculo
            break;
        }

        if escolha == 5 {
            limpar_tela();  // Limpa a tela antes de mostrar o último cálculo
            let (tipo, resultado) = calc.last_calc();
            println!("Último cálculo realizado: {} = {}", tipo, resultado);
            continue;
        }

        limpar_tela();  // Limpa a tela antes de mostrar o último cálculo
        println!("Digite o primeiro número:");
        let x = ler_numero();
        println!("Digite o segundo número:");
        let y = ler_numero();
        limpar_tela();  // Limpa a tela antes de mostrar o último cálculo

        match escolha {
            1 => println!("Resultado da Soma: {}", calc.soma(x, y)),
            2 => println!("Resultado da Subtração: {}", calc