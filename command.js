const Koa = require('koa')
const Router = require('koa-router')
const bodyParser = require('koa-bodyparser')
const ed = require('noble-ed25519')

const config = require('./config.json')

const app = new Koa()
const router = new Router()

app.use(bodyParser());

const publicKey = config.publicKey

// response
router.post('/', verify, async( ctx, next ) => {
  // console.log(ctx.request.body.data.options)
  if(!ctx.request.body) return
  switch(ctx.request.body.type) {
    case 1:
      return ctx.body = { type: 1 }
    case 2:
      // commands
      // if(ctx.request.body.channel_id !== '705218576021192726') return
      switch(ctx.request.body.data.name) {
        case 'thanks':
          return ctx.body = { type: 3, data: {
            tts: false,
            content: `<@${ctx.request.body.member.user.id}>님이 <${ctx.request.body.data.options[0].value}>님에게 감사를 표합니다!`,
            flags: 1 << 1
          } }
        case '고양이':
          return ctx.body = {
            type: 4, data: {
              content: `https://cataas.com/cat?fakeQueryString=${ctx.request.body.id}&size=${ctx.request.body.data.options[0].value}`
            }
          }
      }
  }
})


async function verify(ctx, next) {
  
  const signed = await ed.verify(ctx.request.headers['x-signature-ed25519'], Buffer.concat([Buffer.from(ctx.request.headers['x-signature-timestamp']), Buffer.from(JSON.stringify(ctx.request.body))]), publicKey )
  console.log(signed)
  if(!signed) {
    ctx.status = 403
    return ctx.body = { success: false, error: "Forbidden", code: 403 }
  }
  next()
}
app.use(router.routes()).use(router.allowedMethods())

app.listen(config.port || 8918)
