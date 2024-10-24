document.getElementById('ruleForm').onsubmit = async function(e) {
    e.preventDefault();
    const ruleString = document.getElementById('ruleInput').value;

    const response = await fetch('http://127.0.0.1:5000/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule_string: ruleString })
    });

    const result = await response.json();
    alert(result.message || 'Failed to create rule');
};

document.getElementById('evaluateForm').onsubmit = async function(e) {
    e.preventDefault();
    const userData = document.getElementById('userDataInput').value;

    const response = await fetch('http://127.0.0.1:5000/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_data: JSON.parse(userData) })
    });

    const result = await response.json();
    document.getElementById('result').textContent = `Evaluation Result: ${result.result}`;
};
