module.exports = {
	setupRandomUser: setupRandomUser,
}

function setupRandomUser(context, events, done) {
	let user = pickRandomUser();

	console.log(user);
	
	context.vars['username'] = user['username'];
	context.vars['password'] = user['password'];
	return done();
}

function pickRandomUser() {
	let jsonData = require('./api/users.json');

	let user = jsonData[Math.floor(Math.random() * jsonData.length)];
	return user;
}