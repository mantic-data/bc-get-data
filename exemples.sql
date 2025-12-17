-- {"metric": "facture.montant", "aggregation": "sum"}
SELECT SUM(amount) FROM facture;

-- {
--  "metric": "facture.amount",
--  "aggregation": "sum",
--  "filters": [
--    {"on": "facture.montant", "op": "<", "value": "1000.00"},
--    {"on": "facture.type", "op": "in", "value": "Shodan"}
--  ]
--}
SELECT SUM(amount) FROM facture WHERE facture.amount < 1000.00 AND facture.type LIKE '%Shodan%';

-- {
--  "metric": "facture.montant",
--  "aggregation": "sum",
--  "filters": [
--    {"on": "facture.amount", "op": ">", "value": "9999.99"},
--  ]
--  "group_by": [
--    "facture.type",
--    "facture.service"
--  ]
--}

SELECT SUM(facture.amount), facture.type, facture.service_id
FROM facture
WHERE facture.amount > 9999.99
GROUP BY facture.type, facture.service_id;

--{
--  "metric": "facture.amount",
--  "aggregation": "sum",
--  "filters": [
--    {"on": "service.name", "op": "in", "value": "Artificial Intelligence"},
--  ]
--  "group_by": [
--    "client.name"
--  ]
--}
SELECT SUM(facture.amount), client.id
FROM facture 
	JOIN service ON service.id = facture.service_id
	JOIN client ON client.id = facture.client_id
WHERE service.name LIKE '%Artificial Intelligence%'
GROUP BY client.id;