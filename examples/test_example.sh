echo "test zhpy as script:"
zhpy -c "印出 '哈囉'"
zhpy -c "打印 '哈啰'"

echo "test zhpy examples:"

echo "zhpy hello example..."

cd hello
echo "simple command zhpy [in]"
zhpy hello.twpy
echo "command shortcut zhpy [in] [out]"
zhpy hello.twpy n_hello.py
echo "hello example:"
zhpy -p hello.twpy
cd ..

echo "zhpy in/out example..."
cd inout
zhpy -i inout.twpy -o n_inout.py
zhpy -p inout.twpy
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