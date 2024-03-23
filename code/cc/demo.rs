fn main() {
    let mut count: i64 = 0;
    loop {
        count += 1;
        if (count % 1000000000) == 0 {
            println!("{}\r", count);
        }
    }
}