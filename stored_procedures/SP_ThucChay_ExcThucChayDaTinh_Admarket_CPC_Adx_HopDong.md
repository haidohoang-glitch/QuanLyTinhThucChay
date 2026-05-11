# Stored Procedure: `ThucChay_ExcThucChayDaTinh_Admarket_CPC_Adx_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-04-18 18:05:18.693000
- **Ngày sửa cuối**: 2018-04-21 10:49:38.277000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_ExcThucChayDaTinh_Admarket_CPC_Adx_HopDong]
	@NgayThucHien DATETIME
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE 	@user_id nvarchar(100) ,
	@username nvarchar(100) ,
	@isnoibo nvarchar(100) ,
	@contract_number nvarchar(100) ,
	@promotion nvarchar(100) ,
	@domain_name nvarchar(100) ,
	@domain_tt_click int ,
	@domain_tt_view int ,
	@domain_money money,
	@domain_promotion money,
	@DmSanPhamREF nvarchar(100) ,
	@TenSanPham nvarchar(100) ,
	@DmViTriREF nvarchar(100) ,
	@TenViTri nvarchar(100) 

	DECLARE @ThucChay_adx_cpc_hopdong TABLE
	(
		users_id NVARCHAR(100) ,
		username NVARCHAR(100) ,
		isnoibo NVARCHAR(100) ,
		contract_number NVARCHAR(100) ,
		dsnhanhangid NVARCHAR(200),
		promotion NVARCHAR(100) ,
		domain_name NVARCHAR(100) ,
		domain_tt_click INT ,
		domain_tt_view INT ,
		domain_money MONEY,
		domain_promotion MONEY,
		DmSanPhamREF NVARCHAR(100) ,
		TenSanPham NVARCHAR(100) ,
		DmViTriREF NVARCHAR(100) ,
		TenViTri NVARCHAR(100) 
	)

	DECLARE @phanbo TABLE
	(
		phanbo_id int,
		hopdong_id int,
		nhan_phanbo nvarchar(max),
		nhan_thucchay nvarchar(max),
		thanhtien_phanbo money,
		thanhtienthucchay_phanbo MONEY,
		tk_id nvarchar(100),
		tk_name  nvarchar(100),
		stt int
	)
	--DANH SACH CAC HOP DONG CAN TINH THUC CHAY
	INSERT INTO @ThucChay_adx_cpc_hopdong
	(
	    users_id,
	    username,
	    isnoibo,
	    contract_number,
	    dsnhanhangid,
	    promotion,
	    domain_name,
	    domain_tt_click,
	    domain_tt_view,
	    domain_money,
	    domain_promotion,
	    DmSanPhamREF,
	    TenSanPham,
	    DmViTriREF,
	    TenViTri
	)
	SELECT user_id, username, isnoibo, contract_number, '' dsnhanhangid
	, promotion, domain_name, domain_tt_click
	, domain_tt_view, domain_tt_money, domain_tt_promotion
	, DmSanPhamREF, TenSanPham, DmViTriREF, TenViTri 
	FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong
	WHERE contract_number <> ''
	AND NgayThucHien = @NgayThucHien
	--1. LAY THONG TIN CAC BAN GHI CO HOP DONG CUA SAN PHAM CPC, ADX
	DECLARE db_cursor_hopdong CURSOR FOR
		SELECT users_id,
	    username,
	    isnoibo,
	    contract_number,
	    dsnhanhangid,
	    promotion,
	    domain_name,
	    domain_tt_click,
	    domain_tt_view,
	    domain_money,
	    domain_promotion,
	    DmSanPhamREF,
	    TenSanPham,
	    DmViTriREF,
	    TenViTri FROM @ThucChay_adx_cpc_hopdong
		ORDER BY contract_number, username

	OPEN db_cursor_hopdong  
	FETCH NEXT FROM db_cursor_hopdong INTO @user_id  ,
									@username  ,
									@isnoibo  ,
									@contract_number ,
									@promotion  ,
									@domain_name  ,
									@domain_tt_click  ,
									@domain_tt_view  ,
									@domain_money ,
									@domain_promotion ,
									@DmSanPhamREF  ,
									@TenSanPham  ,
									@DmViTriREF  ,
									@TenViTri   

	WHILE @@FETCH_STATUS = 0  
	BEGIN  
		--2. XAC DINH THONG TIN DOMAIN_ID
	    PRINT @contract_number
		DECLARE @nhan_thucchay_id nvarchar(max), @domain_ref int, @row_count int, @row_index int = 1
		set @domain_ref = dbo.GetWebsiteIDByDomainName(@domain_name)
		IF isnull(@domain_ref,0)=0
		BEGIN
			INSERT INTO dbo.DmWebsiteReportingdb
				(
				TenWebsite,
				CreatedBy,
				CreatedAt,
				LastModifiedBy,
				LastModifiedAt,
				DeletedStatus,
				PrintStatus,
				RecordStatus,
				ID
				)
			VALUES
				(
				@domain_name,	-- TenWebsite - nvarchar(200)
				N'asd',	-- CreatedBy - nvarchar(50)
				GETDATE(),	-- CreatedAt - datetime
				N'asd',	-- LastModifiedBy - nvarchar(50)
				GETDATE(),	-- LastModifiedAt - datetime
				0,	-- DeletedStatus - int
				0,	-- PrintStatus - int
				0,	-- RecordStatus - int
				N'New' -- ID - nvarchar(50)
				)		
			SET @domain_ref = @@IDENTITY
		  END
		  --3. XAC DINH HOPDONGCHITIET: KEY(HOPDONG,SANPHAM, ACCOUNT, GIATRI_THUCCHAYCOTHEGHINHAN)
		  insert into @phanbo
		  (
		      phanbo_id,
		      hopdong_id,
		      nhan_phanbo,
		      nhan_thucchay,
		      thanhtien_phanbo,
		      thanhtienthucchay_phanbo,
		      tk_id,
		      tk_name,
		      stt
		  )
			SELECT hdct.HopDongChiTietID
			, hdct.HopDongFK
			, hdct.DanhSachNhanHangREF
			, '' DanhSachNhanHangChayREF
			, hdct.ThanhTien
			, hdct.ThanhtienThucChay
			, hdct.TK_AdMarketID
			, hdct.TK_AdMarket
			, row_number() over(order by hdct.HopDongChiTietID) FROM 
			(
				SELECT hd.HopDongID, hd.SoHopDong FROM dbo.HopDong hd 
				WHERE hd.SoHopDong = @contract_number
				AND hd.TrangThaiHopDong NOT IN (0,3)
				AND hd.DeletedStatus = 0
			) hd INNER JOIN 
			(
				SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DanhSachNhanHangREF
				, hdct.DmSanPhamREF
				, hdct.TK_AdMarket, hdct.TK_AdMarketID 
				, hdct.ThanhTien, hdct.ThanhtienThucChay
				FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.DeletedStatus = 0 
				AND hdct.DmSanPhamREF = @DmSanPhamREF 
				AND hdct.TK_AdMarketID = @user_id
			)hdct ON hdct.HopDongFK = hd.HopDongID

		
		  --3.1 NEU CO HOPDONGCHITIET PHU HOP THEO TIEU CHI
		  --3.1.1 NEU GHI NHAN DUOC TOAN BO GIA TRI THUCCHAY
		  --3.1.2 NEU CHI GHI NHAN DUOC 1 PHAN THI PHAN CON LẠI CHO VAO ONLINE (PHAN NAY CO LUU LAI THONG TIN HOPDONG, SANPHAM, ACCOUNT, TYPE_ADX, ID, GIATRI, GHICHU)
		  --3.1.3 NEU CO GIA TRI THUC CHAY GHI VAO HOPDONGCHITIET THI DUNG VONG LAP GHI NHAN CHO TUNG HOPDONGCHITIET PHU HOP VA UU TIEN THEO (TYPE_ADX - NEN TANG, DOTCHAY, HOPDONGCHITIETID)
		  --3.2 NEU KHONG CO HOPDONGCHITIET PHU HOP THI THUC HIEN GHI NHAN TOAN BO GIA TRI VAO ONLINE (PHAN NAY CO LUU LAI THONG TIN HOPDONG, SANPHAM, ACCOUNT, TYPE_ADX, ID, GIATRI, GHICHU)

		 -- set @nhan_thucchay = STUFF(( SELECT ',' + CONVERT(NVARCHAR(100), nhanhang_id)
   --                                         FROM 
			--										SELECT DISTINCT dmnhanhang_id 
			--										FROM @ThucChay_adx_cpc_hopdong
			--										WHERE 1 = 1
			--											AND contract_number = @contract_number
			--											AND DmSanPhamREF = @DmSanPhamREF
			--											AND [user_id] = @user_id
			--											AND dmnhanhang_id <> '0'
			--								)
   --                                         GROUP BY nhanhang_id
   --                                         FOR XML PATH('')
   --                                         ), 1, 1, '')
															  
			--if isnull(@nhan_thucchay,'') =  ''
			--	update  @phanbo set nhan_thucchay = nhan_phanbo 
			--else
			--	update  @phanbo set nhan_thucchay = @nhan_thucchay 
		    --VONG LAP DE XAC DINH DIEU KIEN LUU GIA TRI CHO TUNG BAN GHI
		  

		  FETCH NEXT FROM db_cursor_hopdong INTO @user_id  ,
									@username  ,
									@isnoibo  ,
									@contract_number ,
									@promotion  ,
									@domain_name  ,
									@domain_tt_click  ,
									@domain_tt_view  ,
									@domain_money ,
									@domain_promotion ,
									@DmSanPhamREF  ,
									@TenSanPham  ,
									@DmViTriREF  ,
									@TenViTri   
	END 

	CLOSE db_cursor_hopdong  
	DEALLOCATE db_cursor_hopdong 
	
	

END


```
