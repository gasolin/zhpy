rm -rf hello/*.py
rm -rf inout/*.py
rm -rf loop/*.py
rm -rf game/*.py

echo "test zhpy as script, total: 2"
zhpy -c "印出 '哈囉'"
zhpy -c "打印 '哈啰'"

echo "test zhpy examples: total: 12"

echo "zhpy hello example..."

cd hello
echo "simple command zhpy [in]:"
zhpy hello.twpy
echo "input command zhpy [in]:"
zhpy -i hello.twpy
echo "input command zhpy [in] [encoding]:"
zhpy -i hello.twpy -e 'utf8'
echo "hello example:"
zhpy -p hello.twpy
echo "big5 example:"
zhpy -p hello_big5.twpy
echo "gbk example:"
zhpy -p hello_gb.cnpy
echo "run hello as script with arguments:"
./hello_arg.twpy hello world
cd ..

echo "zhpy in/out example..."
cd inout
zhpy -i inout.twpy -o n_inout.py
zhpy -p inout.twpy
echo "run in/out as script:"
./inout
cd ..

echo "zhpy loop example..."
cd loop
zhpy -p tabl.twpy
zhpy -p contact.cnpy
cd ..

echo "zhpy game example..."
echo "it's an optional test, pygame module required. Use 'Ctrl+c' to escape"

cd game
zhpy -p game.twpy
cd ..

echo "finish"