# Primeiros Passos em SQL e NoSQL

Tópicos abordados:
- SQL
	- Tabelas, Colunas e Registros;

	- Operações Nativas;
		- Insert;
		- Select;
		- Update;
		- Delete;
		- Alter;
		- Delete;
		- Drop.

	- Chave Primária e Estrangeira;

	- Normalização de Dados;

	- Junções e Subconjuntos;

	- Funções Agregadas e Agrupamentos de Resultados.

- NoSQL
	- Vantagens e Desvantagens do NoSQL,

	- Tipos de SGBD,
		- Key-Value,
		- Documento,
		- Coluna,
		- Grafos,
		- etc.
	
	- Tipos de Dados,
		- String,
		- Number,
		- Date,
		- Null,
		- ObjectId,
		- Array,
		- Documento Embutido,
		- Referência,
		- GeoJSON.

	- Operações Nativas,
		- Criar Database,
			- use{{nome_banco_de_dados}}.

		- Criar uma Collection,
			- db.createCollection("nome_collection").

		- Inserir Documentos,
			- db.nome_coleção.insertOne({}),
			- db.nome_coleção.insertMany([{}]).

		- Consultar Documentos,
			- db.nome_coleção.find({}),
			- db.nome_coleção.findOne({}),
		- db.nome_coleção.findOneAndUpdate({valor_antigo}, {$set:{valor_novo}}),
			- db.nome_coleção.findOneAndDelete({}).

		- Atualizar Documentos,
			- db.nome_coleção.updateOne(),
			- db.nome_coleção.updateMany(),
			- db.nome_coleção.replaceOne().

		- Operadores de Update,
			- $inc,
			- $push,
			- $set,
			- $unset,
			- $rename.

		- Excluir Documentos.
			- db.nome_coleção.deleteOne({}),
			- db.nome_coleção.deleteMany({}).

	- Operadores,
		- Igualdade,
			- db.nome_coleção.find({}).
		- Lógicos,
			- $and,
			- $or,
			- $not.
		- Comparação,
			- $eq:  ==,
			- $ne:  !=,
			- $gt:  >,
			- $gte: >=,
			- $lt:  <,
			- $lte: <=,
			- $in:  [],
			- $nin: [].

	- Ordenação,

	- Limitação,
	
	- Paginação.