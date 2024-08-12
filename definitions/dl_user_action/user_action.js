const project = "your_project";
const csvFileName = "sample/user_action.csv";

publish("user_action_jsver", {
  type: "view",
  schema: "dl_user_action",
  tags: ["dl_user_action"],
  description: "user-actionのraw data (JavaScript version)",
})
  .query(ctx => `
CREATE OR REPLACE EXTERNAL TABLE \`${project}.datalake.user_action_jsver\` (
  timestamp STRING,
  user_id STRING,
  session_id STRING,
  page_url STRING,
  event_type STRING,
  device_type STRING,
  browser STRING
)
OPTIONS (
  description = "user-actionのraw data (JavaScript version)",
  uris = ['gs://${project}-dataform/${csvFileName}'],
  format = 'CSV',
  skip_leading_rows = 1
)
  `);