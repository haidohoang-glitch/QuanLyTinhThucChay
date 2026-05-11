# Stored Procedure: `prc_asd_TinhGiaTri_ThayDoi_HopDong_Per_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:02:39.620000
- **Ngày sửa cuối**: 2024-10-25 11:50:42.007000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDong_ID` | `int(4)` | No |
| `@PhanBo_ID` | `int(4)` | No |
| `@DmSanPham_ID` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@GiaTriTaiThoiDiemTinhThucChay` | `money(8)` | No |
| `@GiaTriGanNhatThayDoi` | `money(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>

-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_TinhGiaTri_ThayDoi_HopDong_Per_PhanBo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime,
	@HopDong_ID int,
	@PhanBo_ID int,
	@DmSanPham_ID int,
	@TenSanPham nvarchar(200),
	@GiaTriTaiThoiDiemTinhThucChay money,
	@GiaTriGanNhatThayDoi money
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @SoHopDong nvarchar(50),@GiaTriOnline money
	,@User_id nvarchar(50), @User_Name nvarchar(100), @data_type INT = 0
	declare @DonViTinh nvarchar(50) = N'CPC'
	declare @GiaTriThucChayPhanBo money = 0

	select top 1 @User_id = TK_AdMarketID,@User_Name = TK_AdMarket from HopDongChiTiet where HopDongChiTietID = @PhanBo_ID
	select TOP (1) @SoHopDong = SoHopDong from HopDong 
	Where HopDongID = @HopDong_ID

	set @GiaTriThucChayPhanBo = isnull((select SUM(isnull(GiaTriThayDoi,0)+isnull(ThanhTienSauTrietKhauThucChay,0)) 
										from ThucChayDaTinhAdmarket
										where HopDongChiTietREF = @PhanBo_ID and DmSanPhamREF = @DmSanPham_ID)
									,0)
	--1. TH NEU TANG GIA TRI PHAN BO
	IF(@GiaTriTaiThoiDiemTinhThucChay > @GiaTriGanNhatThayDoi )
	BEGIN
		--1.1 NEU TON TAI TIEN CUA PHAN BO TRONG TABLE dbo.ThucChayAdmarket_HopDong_online
		IF(EXISTS( SELECT top 1 HopDongChiTietREF  from [dbo].ThucChayAdmarket_HopDong_online 
			where contract_number = @SoHopDong 
			and HopDongChiTietREF = @PhanBo_ID
			and trangthai = 0
			and DmSanPhamREF = @DmSanPham_ID
			and [user_id] = @User_id
			and confirm_status <> -1))
			BEGIN
				--PRINT 'START'
				--1. TH1: TINH CHO TH CO PHAN BO
				DECLARE  @max_count int, @count_index int = 1;
				create table #ThucChayAdmarket_HopDong_Online_temp
				(
					[user_id] [nvarchar](100) NULL,
					[username] [nvarchar](100) NULL,
					[isnoibo] [nvarchar](100) NULL,
					[contract_number] [nvarchar](100) NULL,
					[promotion] float NULL,
					[domain_name] [nvarchar](100) NULL,
					[domain_tt_click] [int] NULL,
					[domain_tt_view] [int] NULL,
					[domain_money] [float] NULL,
					[domain_promotion] [float] NULL,
					[HopDongChiTietREF] [int] NULL,
					[DmSanPhamREF] int NULL,
					[TenSanPham] [nvarchar](100) NULL,
					[DmViTriREF] [int] NULL,
					[TenViTri] [nvarchar](100) NULL,
					[NgayThucHien] [datetime] NULL,
					[NhanHang] [nvarchar](100) NULL,
					stt [int],
					status_record [smallint]
				)

				insert into #ThucChayAdmarket_HopDong_Online_temp 
				SELECT 
					distinct
					[user_id] ,
					[username] ,
					[isnoibo],
					[contract_number],
					convert(float,[promotion]),
					[domain_name],
					sum(convert(int,domain_tt_click)),
					sum(convert(int,domain_tt_view)),
					sum(convert(float,domain_money)),
					sum(convert(float,domain_promotion)),
					HopDongChiTietREF,
					[DmSanPhamREF],
					[TenSanPham],
					convert(int,[DmViTriREF]),
					[TenViTri],
					@NgayThucHien,
					isnull(NhanHang,''),
					row_number() over(order by [user_id]),
					0 status_record -- 0 trang thai chua duoc tinh, 1 trang thai da duoc tinh
			 		FROM dbo.ThucChayAdmarket_HopDong_online
				WHERE HopDongChiTietREF = @PhanBo_ID
				AND domain_money >0
				AND [DmSanPhamREF] = @DmSanPham_ID
				AND [user_id] = @User_id
				AND trangthai = 0
				group by	[user_id] ,
							[username] ,
							[isnoibo],
							[contract_number],
							[promotion],
							[domain_name],
							[HopDongChiTietREF],
							[DmSanPhamREF],
							[TenSanPham],
							[DmViTriREF],
							[TenViTri],
							NhanHang

			
				--------------------------------------------------------------------------------------------------
				-- tong so luong ban ghi
				select @max_count = count(1) from #ThucChayAdmarket_HopDong_Online_temp;
	
				--------------------------------------------------------------------------------------------------
				declare	@username nvarchar(100) ,
						@isnoibo nvarchar(100) ,
						@contract_number nvarchar(100) ,
						@promotion float ,
						@domain_name nvarchar(100) ,
						@domain_tt_click int ,
						@domain_tt_view int ,
						@domain_money float,
						@domain_promotion float,
						@HopDongChiTietREF int,
						@DmSanPhamREF int ,
						@DmViTriREF int ,
						@TenViTri nvarchar(100) ,
						@NgayTinh datetime ,
						@NhanHang nvarchar(100),
						@Status_record smallint

				declare @giatrihopdong float, @thanhtienthucchayhopdong float, @giatrithucchaythua float,
						@tientinhthucchay float, @tiendovaoonline float = 0,
						@domain_tt_click_online int, @domain_tt_view_onlie int;

				while @count_index <= @max_count
				BEGIN
					--print @count_index
					SELECT 
							@user_id = [user_id] ,
							@username = username ,
							@isnoibo = isnoibo,
							@contract_number  = contract_number,
							@promotion = promotion,
							@domain_name = domain_name,
							@domain_tt_click = domain_tt_click,
							@domain_tt_view = domain_tt_view,
							@domain_money = domain_money,-- gia tri tra ve khong bao gom vat
							@domain_promotion = domain_promotion,
							@HopDongChiTietREF = HopDongChiTietREF,
							@DmSanPhamREF = DmSanPhamREF,
							@TenSanPham = TenSanPham,
							@DmViTriREF = DmViTriREF,
							@TenViTri = TenViTri ,
							@NgayTinh = NgayThucHien,
							@NhanHang = nhanhang
					from #ThucChayAdmarket_HopDong_Online_temp where stt = @count_index and domain_money >0;

					declare @GhiChu nvarchar(2000) = N'', @domain_ref int = 0, @DmMaHopDongREF int =0, @TenMaHopDong nvarchar(100) = N''
		
					IF((@isnoibo = 1) or (@contract_number like 'NB%' or @contract_number like 'SH%' or @contract_number like 'S-NB%'))
					BEGIN
						SET @DmMaHopDongREF = 310
						SET @TenMaHopDong = N'NB'
					END
					ELSE
					BEGIN
						SET @DmMaHopDongREF = 0
						SET @TenMaHopDong = ''
					END
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

					set @tientinhthucchay = @domain_money
					--1.2.1 TH: CO SOHOPDONG NHUNG KHONG CO PHANBO CAN TINH
					if not exists(SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd 
								INNER JOIN dbo.HopDongChiTiet hdct ON hd.Hopdongid = hdct.HopDongFk
								WHERE hd.SoHopDong = @contract_number 
								AND hdct.HopDongChiTietID = @HopDongChiTietREF 
								AND hdct.DmSanPhamREF = @DmSanPhamREF
								AND hdct.tk_admarketid = @user_id
								AND hdct.deletedstatus = 0 ORDER BY hdct.HopDongChiTietID
					)
					begin
						set @data_type = 1;
						set @tiendovaoonline = @domain_money;
						set @domain_tt_click_online = @domain_tt_click;
						set @domain_tt_view_onlie = @domain_tt_view;
					end
					--1.2.2 TH: CO SOHOPDONG VA CO PHANBO CAN TINH
					else
					begin

						select top 1 @giatrihopdong = sum(isnull(ThanhTien,0)) from dbo.hopdongchitiet where 
						dmSanPhamREF = @DmSanPhamREF and deletedstatus = 0 and TK_AdMarket = @username and
						hopdongchitietid = @HopDongChiTietREF;

						select top 1 @thanhtienthucchayhopdong = sum(isnull(thanhtiensautrietkhauthucchay+GiaTriThayDoi,0))  
						from dbo.thucchaydatinhadmarket where sohopdong = @contract_number 
						and dmSanPhamREF = @DmSanPhamREF
						and HopDongChiTietREF = @HopDongChiTietREF

						set @thanhtienthucchayhopdong = isnull(@thanhtienthucchayhopdong,0);
						set @giatrihopdong = isnull(@giatrihopdong,0)

						--- TH: NEU GIA TRI THUCCHAYDATINH >= THANHTIENPHANBO
						if @giatrihopdong - @thanhtienthucchayhopdong <=0 
						begin 
							--Neu ThanhTienThucChay >= ThanhTienPhanBo
							BREAK; 
						end 

						---TH: GIA TRI THUCCHAYDATINH < THANHTIENPHANBO VA GIATRITHUCCHAY KHONG DO DUOC FULL VAO PHANBO
						if (@giatrihopdong - @thanhtienthucchayhopdong >0) and (@giatrihopdong - @thanhtienthucchayhopdong - @domain_money) <=0 
						begin
							DECLARE @TienThucChayThucThu FLOAT = 0
							SET @tiendovaoonline =  @domain_money + @thanhtienthucchayhopdong - @giatrihopdong;
							SET @domain_tt_click_online = @domain_tt_click;
							SET @domain_tt_view_onlie = @domain_tt_view; 
							SET @TienThucChayThucThu = @domain_money - @tiendovaoonline

							--print N'TH: GIA TRI THUCCHAYDATINH < THANHTIENPHANBO VA GIATRITHUCCHAY KHONG DO DUOC FULL VAO PHANBO'

							SET @GhiChu = N'Thuc_Chay_Admarket_PhanBo_online tăng gt hợp đồng, không đổ full giá trị online'

							-- B1: -- insert dl vao table canhbao [ThucChayAdmarket_HopDong_online] 
							exec [dbo].[prc_insert_ThucChayAdmarket_HopDong_online_PhanBo]     @user_id ,
								@username ,
								@isnoibo ,
								@contract_number ,
								@promotion ,
								@domain_name ,
								@domain_tt_click_online ,
								@domain_tt_view_onlie ,
								@tiendovaoonline ,
								@domain_promotion ,
								0 ,
								@HopDongChiTietREF,
								@DmSanPhamREF ,
								@TenSanPham,
								@DmViTriREF ,
								@TenViTri,
								@NgayThucHien  ,
								@DonViTinh,
								@NhanHang,
								@data_type 
			
							----cho nay can xem lai haidh 11/03/2024 vi tien nay truoc do da co trong online roi
							----B2: Thuc hien insert dl thucchay online vao table ThucChayDaTinhAdmarket, DotChayHopDong = 'Thuc_Chay_Admarket_PhanBo_online', SoLuongDotChayHD = @HopDongChiTietREF, 
							---- SoLuongDotChayBooking =2,3: canh bao dl tra ve vuot qua gt hop dong; 1: Hopdong ko co phabo phu hop tinh, 0 online bt

		
							--B2: Tinh du lieu theo chieu hopdongchitiet
							exec [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong_PhanBo]
								@NgayThucHien			= @NgayTinh,
								@SoHopDong				= @contract_number,
								@PhanBoID				= @HopDongChiTietREF,
								@DmSanPhamREF			= @DmSanPhamREF,
								@TenSanPham				= @TenSanPham,
								@DmWebsiteREF			= @domain_ref,
								@TenWebsite				= @domain_name,
								@TongViewThucChay		= @domain_tt_view,
								@TongClickThucChay		= @domain_tt_click,
								@SoLuongThucChay		= @domain_tt_click,
								@ThanhTienThucChay		= @TienThucChayThucThu,
								@SoLuongThucChayKM		= 0,
								@ThanhTienThucChayKM	= 0,
								@SoLuongLechTreoHa		= 0,
								@ThanhTienLechTreoHa	= 0,
								@TypeInsert				= 1, -- 1: ThucChay; 2: KhuyenMai; 3 LechTreoHa
								@DonViTinhSanPham		= @DonViTinh,
								@GhiChu					= @GhiChu,
								@DmViTriREF				= @DmViTriREF,
								@TenViTri				= @TenViTri,
								@DmNhanHangREF			= @NhanHang

								
							-- B3: UPDATE trang thai cho table ThucChayAdmarket_HopDong_online trangthai = 1 --da xl
							UPDATE dbo.ThucChayAdmarket_HopDong_online
							SET trangthai = 1,  NgayThucHien = @NgayThucHien
							, confirm_date = getdate()
							WHERE HopDongChiTietREF = @PhanBo_ID
							AND [DmSanPhamREF] = @DmSanPham_ID
							AND [user_id] = @User_id
							AND [domain_name] = @domain_name
							AND [DmViTriREF] = @DmViTriREF
							AND NhanHang = @NhanHang
							AND [isnoibo] = @isnoibo
							and trangthai = 0
							--B4: THOAT VONG LAP
							BREAK; 

						end
						--- TH: GIATRITHUCCHAY DO FULL DUOC VAO PHANBO N'Thuc_Chay_Admarket Đổ online tăng gt hợp đồng 2'
						if @giatrihopdong - @thanhtienthucchayhopdong - @domain_money >=0
						begin
							--print N'TH: GIATRITHUCCHAY DO FULL DUOC VAO PHANBO Thuc_Chay_Admarket Đổ online tăng gt hợp đồng 2'
							
					
							-- B0: thuc hien insert thanhtienthucchay vao ThucChayDaTinhAdmarket theo phanbo
							SET @GhiChu = N'Thuc_Chay_Admarket_PhanBo_online tăng gt hợp đồng'

							EXEC [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong_PhanBo]
								@NgayThucHien			= @NgayTinh,
								@SoHopDong				= @contract_number,
								@PhanBoID				= @HopDongChiTietREF,
								@DmSanPhamREF			= @DmSanPhamREF,
								@TenSanPham				= @TenSanPham,
								@DmWebsiteREF			= @domain_ref,
								@TenWebsite				= @domain_name,
								@TongViewThucChay		= @domain_tt_view,
								@TongClickThucChay		= @domain_tt_click,
								@SoLuongThucChay		= @domain_tt_click,
								@ThanhTienThucChay		= @domain_money,
								@SoLuongThucChayKM		= 0,
								@ThanhTienThucChayKM	= 0,
								@SoLuongLechTreoHa		= 0,
								@ThanhTienLechTreoHa	= 0,
								@TypeInsert				= 1, -- 1: ThucChay; 2: KhuyenMai; 3 LechTreoHa
								@DonViTinhSanPham		= @DonViTinh,
								@GhiChu					= @GhiChu,
								@DmViTriREF				= @DmViTriREF,
								@TenViTri				= @TenViTri,
								@DmNhanHangREF			= @NhanHang

								-- B1: UPDATE trang thai cho table ThucChayAdmarket_HopDong_online trangthai = 1 --da xl
								UPDATE dbo.ThucChayAdmarket_HopDong_online
								SET trangthai = 1,  NgayThucHien = @NgayThucHien
								, confirm_date = getdate()
								WHERE HopDongChiTietREF = @PhanBo_ID
								AND [DmSanPhamREF] = @DmSanPham_ID
								AND [user_id] = @User_id
								AND [domain_name] = @domain_name
								AND [DmViTriREF] = @DmViTriREF
								AND NhanHang = @NhanHang
								AND [isnoibo] = @isnoibo
								and trangthai = 0

						end
					end 

					set @count_index +=1;
					--------------------------------------------------------------------------------------------------
					
				END

				drop table #ThucChayAdmarket_HopDong_Online_temp;
			END
	END
	--2. TH NEU GIAM GIA TRI PHAN BO MA VƯƠT KHONG QUA 1000 (DO LAM TRON SO TRONG QUA TRINH TINH) THI THUC HIEN XL - haidh comment 21/10/2024
	ELSE
	BEGIN
		IF(
			(@GiaTriTaiThoiDiemTinhThucChay < @GiaTriGanNhatThayDoi )
			AND (@GiaTriThucChayPhanBo - @GiaTriTaiThoiDiemTinhThucChay >0 
				AND @GiaTriThucChayPhanBo - @GiaTriTaiThoiDiemTinhThucChay < 1000)
		)
		BEGIN
			DECLARE @DmWebsiteREF INT, @TenWebsite NVARCHAR(50),@v_TenViTri nvarchar(50)
				DECLARE @v_DmViTriREF INT
				DECLARE @GiaTriThayDoi FLOAT = 0, @v_GhiChu NVARCHAR(max) =''
				Declare @v_ThucChayDaTinhID_output nvarchar(50)
				SET @GiaTriThayDoi = @GiaTriTaiThoiDiemTinhThucChay - @GiaTriThucChayPhanBo
				SET @v_DmViTriREF  = '1' --cần sửa 1: AdX  2: AdX Mobile, 3: AdX Ecommerce
				SET @v_TenViTri = 'ADX' -- cần sửa
				SET @DmWebsiteREF = 265
				SET @TenWebsite = '(Blanks)'
				SET @v_GhiChu = N'Update TC'

			--b1. check tt hợp đồng
			SELECT TOP (1) @v_DmViTriREF = DmViTriREF,@v_TenViTri = TenViTri --, DmLoaiBannerREF, TenLoaiBanner, CreatedAt  
			FROM dbo.ThucChayDaTinhAdmarket
			WHERE HopDongChiTietREF= @PhanBo_ID
			ORDER BY LastModifiedAt DESC

			SET @v_DmViTriREF = ISNULL(@v_DmViTriREF,0)
			SET @v_TenViTri = ISNULL(@v_TenViTri, 'Khong ton tai')

			-- b2 chạy câu lệnh xl 
			EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline_v2]
				@NgayThucHien							= @NgayThucHien, --cần sửa
				@ThucChay_PerformanceBase_ThayDoi_ID	= 0,
				@HopDongID								= @HopDong_ID																																																																																																																																																																						,--cần sửa																																																															,
				@HopDongChiTietID						= @PhanBo_ID, -- cần sửa
				@DmSanPhamREF							= @DmSanPham_ID,  -- cần sửa ADX: 585, Viewplus 628
				@Tk										= @User_Name,  -- cần sửa
				@DmViTriREF								= @v_DmViTriREF,
				@TenViTri								= @v_TenViTri,
				@DmWebsiteREF							= @DmWebsiteREF,
				@TenWebsite								= @TenWebsite,
				@GiaTriThayDoi							= @GiaTriThayDoi,  -- cần sửa
				@GiaTriKMThayDoi						= 0,
				@GhiChu									= @v_GhiChu,
				@ThucChayDaTinhID_output				= @v_ThucChayDaTinhID_output OUTPUT
		END
	END

END

```
